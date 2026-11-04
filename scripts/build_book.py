#!/usr/bin/env python3
"""Build the private commercial editions from local Markdown and original assets."""
from pathlib import Path
import base64, datetime, hashlib, html, json, os, re, shutil, subprocess, sys, tempfile, zipfile
from bs4 import BeautifulSoup
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from weasyprint import HTML
from pypdf import PdfReader, PdfWriter
from book_common import ROOT,OUTPUT,TITLE,SUBTITLE,AUTHOR,DATE,EPOCH,sources,sections,sha
from build_epub import build_epub


def cover_path():
    path=ROOT/'cover/export/COVER.jpg'
    if path.exists():return path
    found=sorted((ROOT/'cover/export').glob('*.jpg'))
    if not found:raise FileNotFoundError('A JPEG cover is required in cover/export/')
    return found[0]


def uri(path):
    suffix=path.suffix.lower();mime={'.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.svg':'image/svg+xml'}[suffix]
    return 'data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode()


def html_edition():
    docs=sections();toc=[];parts=[]
    for sec in docs:
        soup=BeautifulSoup(sec['html'],'html.parser')
        for img in soup.find_all('img'):
            p=(ROOT/img['src']).resolve()
            if not p.is_relative_to(ROOT):raise ValueError('Asset outside project')
            img['src']=uri(p)
        for a in soup.find_all('a',href=True):
            href=a['href']
            if href.startswith(('https://','http://','mailto:','#')):continue
            target=(ROOT/href).resolve()
            if href.endswith('.md'):
                targetstem=Path(href).stem
                if any(x['name']==targetstem for x in docs):a['href']='#'+targetstem
                else:a['href']='downloads/'+href
            else:a['href']='downloads/'+href
        parts.append(f'<section class="book-section" id="{sec["name"]}">{soup}</section>')
        toc.append(f'<li><a href="#{sec["name"]}">{html.escape(sec["title"])}</a></li>')
    css=(ROOT/'scripts/book.css').read_text()
    title=html.escape(TITLE);subtitle=html.escape(SUBTITLE)
    return f'''<!doctype html><html lang="de-DE"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="author" content="{AUTHOR}"><title>{title}</title><style>{css}</style></head><body><a class="skip" href="#book-content">Zum Buchinhalt</a><header><img class="cover" src="{uri(cover_path())}" alt="Originales Titelbild mit Geschenkbox, CNC-Werkzeug und Laserstrahl"><h1>{title}</h1><p>{subtitle}</p><p>{AUTHOR}</p><p class="edition-note">Technisches Arbeitsmanuskript · {DATE} · Nicht zur kommerziellen Veröffentlichung freigegeben</p></header><nav aria-label="Inhaltsverzeichnis"><h2>Inhalt</h2><ol>{''.join(toc)}</ol></nav><main id="book-content">{''.join(parts)}</main><footer>Ende des Arbeitsmanuskripts. Maschinen-, Rechte-, Autoren- und Verlagsfreigaben stehen aus.</footer></body></html>'''


def normalize_zip(path):
    with zipfile.ZipFile(path) as z:entries={n:z.read(n) for n in z.namelist()}
    if 'docProps/core.xml' in entries:
        entries['docProps/core.xml']=re.sub(rb'(<dcterms:(?:created|modified)[^>]*>)[^<]+',rb'\g<1>2026-11-04T12:00:00Z',entries['docProps/core.xml'])
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
        for name,data in sorted(entries.items()):
            zi=zipfile.ZipInfo(name,(2026,11,4,12,0,0));zi.compress_type=zipfile.ZIP_DEFLATED;zi.external_attr=0o644<<16;z.writestr(zi,data)


def docx_edition(build):
    ref=build/'reference.docx'
    ref.write_bytes(subprocess.check_output(['pandoc','--print-default-data-file','reference.docx']))
    d=Document(ref)
    for sec in d.sections:
        sec.page_width=Cm(21);sec.page_height=Cm(29.7);sec.top_margin=Cm(1.9);sec.bottom_margin=Cm(2);sec.left_margin=Cm(1.8);sec.right_margin=Cm(1.8)
    for name in ['Normal','Body Text','First Paragraph']:
        style=next(s for s in d.styles if s.name==name);style.font.name='DejaVu Sans';style.font.size=Pt(10.2)
        style.paragraph_format.line_spacing=1.35
        style.paragraph_format.space_after=Pt(6)
    for name,size in [('Heading 1',23),('Heading 2',15),('Heading 3',11.5)]:
        style=next(s for s in d.styles if s.name==name);style.font.name='DejaVu Sans';style.font.size=Pt(size);style.font.color.rgb=RGBColor.from_string('142C3A');style.paragraph_format.keep_with_next=True
    next(s for s in d.styles if s.name=='Heading 1').paragraph_format.page_break_before=True
    next(s for s in d.styles if s.name=='Image Caption').font.size=Pt(8)
    d.core_properties.author=AUTHOR;d.core_properties.title=TITLE
    d.save(ref)
    source='\n\n'.join(p.read_text() for p in sources())
    combined=build/'book.md';combined.write_text(source)
    path=OUTPUT/'CNC_Laser_Geschenkbox_Amir_Mobasheraghdam.docx'
    command=['pandoc',str(combined),'-o',str(path),'--standalone','--toc','--toc-depth=1','--resource-path='+str(ROOT),'--reference-doc='+str(ref),'-M','title='+TITLE,'-M','subtitle='+SUBTITLE,'-M','author='+AUTHOR,'-M','lang=de-DE','-M','date='+DATE]
    subprocess.run(command,cwd=ROOT,check=True)
    # Accessible alt text is written by Pandoc; ensure document language at XML level.
    d=Document(path)
    defaults=d.styles.element.find(qn('w:docDefaults'))
    if defaults is not None:
        rpr=defaults.find(qn('w:rPrDefault'))
        if rpr is not None:
            props=rpr.find(qn('w:rPr'))
            if props is None:props=OxmlElement('w:rPr');rpr.append(props)
            lang=props.find(qn('w:lang'))
            if lang is None:lang=OxmlElement('w:lang');props.append(lang)
            lang.set(qn('w:val'),'de-DE')
    d.core_properties.created=datetime.datetime(2026,11,4,12,0,0)
    d.core_properties.modified=datetime.datetime(2026,11,4,12,0,0)
    d.save(path);normalize_zip(path)
    return path


def projects_zip():
    path=OUTPUT/'reader_project_files.zip'
    projectroot=ROOT/'engineering'
    if not projectroot.is_dir():raise FileNotFoundError('engineering/')
    files=[p for p in projectroot.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in ['.pyc']]
    if not files:raise ValueError('No engineered project files')
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(files):
            zi=zipfile.ZipInfo('engineering/'+str(p.relative_to(projectroot)),(2026,11,4,12,0,0));zi.compress_type=zipfile.ZIP_DEFLATED;zi.external_attr=0o644<<16;z.writestr(zi,p.read_bytes())
    return path


def main():
    os.environ.setdefault('SOURCE_DATE_EPOCH',str(EPOCH));os.environ.setdefault('XDG_CACHE_HOME','/tmp/book-font-cache')
    OUTPUT.mkdir(exist_ok=True);build=OUTPUT/'build';build.mkdir(exist_ok=True)
    web=OUTPUT/'web';web.mkdir(exist_ok=True)
    markup=html_edition();(web/'index.html').write_text(markup)
    # Deployable download targets stay within the private web edition.
    downloads=web/'downloads';downloads.mkdir(exist_ok=True)
    for directory in ['engineering','research','publishing']:
        if (ROOT/directory).exists():shutil.copytree(ROOT/directory,downloads/directory,dirs_exist_ok=True,ignore=shutil.ignore_patterns('evidence','__pycache__','*.pyc'))
    pdf=OUTPUT/'CNC_Laser_Geschenkbox_Digital.pdf'
    raw=build/'raw.pdf';HTML(string=markup,base_url=str(ROOT)).write_pdf(raw,pdf_identifier=b'giftbox-working-draft-20261104')
    reader=PdfReader(raw);writer=PdfWriter(clone_from=reader)
    writer.add_metadata({'/Title':TITLE,'/Author':AUTHOR,'/Subject':SUBTITLE,'/CreationDate':'D:20261104120000Z','/ModDate':'D:20261104120000Z'})
    with pdf.open('wb') as f:writer.write(f)
    docx=docx_edition(build);epub=build_epub();projects=projects_zip()
    shutil.copyfile(cover_path(),OUTPUT/'COVER.jpg')
    artifacts=[pdf,docx,epub,projects,web/'index.html',OUTPUT/'COVER.jpg']
    metrics={'date':DATE,'sources':[str(p.relative_to(ROOT)) for p in sources()],'chapters':9,'pdf_pages':len(PdfReader(pdf).pages),'artifacts':{str(p.relative_to(ROOT)):{'bytes':p.stat().st_size,'sha256':sha(p)} for p in artifacts},'word_count':sum(len(re.findall(r'\b[\wÄÖÜäöüß]+\b',p.read_text())) for p in sources()),'reproducibility':'deterministic metadata configured; repeat-build comparison required'}
    (ROOT/'quality').mkdir(exist_ok=True);(ROOT/'quality/build_metrics.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2))
    print(json.dumps(metrics,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
