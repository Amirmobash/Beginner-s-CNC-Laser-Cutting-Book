#!/usr/bin/env python3
"""Meaningful source, image, SVG, DOCX, PDF and standalone-HTML checks."""
import json,re,sys,zipfile
from pathlib import Path
from urllib.parse import unquote,urlsplit
from lxml import etree
from bs4 import BeautifulSoup
from pypdf import PdfReader
from docx import Document
from book_common import ROOT,OUTPUT,sources,sections,AUTHOR


def validate():
    errors=[];checks=[];images=set();captions=0
    try:paths=sources()
    except FileNotFoundError as e:paths=[];errors.append(str(e))
    for p in paths:
        text=p.read_text()
        if len(re.findall(r'\w+',text))<80:errors.append('Substantively empty source: '+p.name)
        for alt,src in re.findall(r'!\[([^\]]*)\]\(([^)]+)\)',text):
            images.add(src)
            if not alt.strip():errors.append('Missing image alt in '+p.name)
            if not re.search(r'F\d{2}',alt):errors.append('Missing stable figure ID/caption: '+src)
            else:captions+=1
            if not (ROOT/src).is_file():errors.append('Missing image: '+src)
        for pattern in [r'\bTODO\b',r'\bLOREM\b',r'\bTBD\b',r'\[AUTOR[^\]]*\]']:
            if re.search(pattern,text):errors.append('Unresolved production placeholder in '+p.name+': '+pattern)
    checks.append({'check':'manuscript_files','count':len(paths)})
    if len(images)<30:errors.append(f'Fewer than 30 meaningful referenced figures: {len(images)}')
    for p in (ROOT/'figures/svg').glob('*.svg'):
        try:
            tree=etree.parse(str(p))
            if not tree.getroot().tag.endswith('svg'):errors.append('Not SVG '+str(p))
        except etree.XMLSyntaxError as e:errors.append('Malformed SVG '+str(p)+': '+str(e))
    docx=OUTPUT/'CNC_Laser_Geschenkbox_Amir_Mobasheraghdam.docx'
    if not docx.is_file():errors.append('Missing DOCX')
    else:
        try:
            doc=Document(docx)
            if len(doc.paragraphs)<100:errors.append('DOCX has insufficient editable paragraphs')
            with zipfile.ZipFile(docx) as z:
                xml=etree.fromstring(z.read('word/document.xml'))
                ns={'wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'}
                props=xml.findall('.//wp:docPr',ns)
                for prop in props:
                    if not (prop.get('descr') or prop.get('title')):errors.append('DOCX image missing alt: '+prop.get('name','?'))
                if len(props)<30:errors.append('DOCX has fewer than 30 embedded instructional images')
                media=[n for n in z.namelist() if n.startswith('word/media/')]
                if len(media)<30:errors.append('DOCX missing embedded media')
            checks.append({'check':'docx_editable','paragraphs':len(doc.paragraphs),'image_instances':len(props),'embedded_media':len(media)})
        except Exception as e:errors.append('DOCX read failure '+str(e))
    pdf=OUTPUT/'CNC_Laser_Geschenkbox_Digital.pdf'
    if not pdf.is_file():errors.append('Missing PDF')
    else:
        try:
            reader=PdfReader(pdf);texts=[p.extract_text() or '' for p in reader.pages]
            if any(len(t.strip())<20 for t in texts):errors.append('PDF contains unexpectedly empty pages')
            if not reader.outline:errors.append('PDF missing bookmarks')
            checks.append({'check':'pdf_searchable','pages':len(texts),'characters':sum(map(len,texts)),'bookmarks':len(reader.outline),'page_target_45_60':45<=len(texts)<=60})
        except Exception as e:errors.append('PDF read failure '+str(e))
    web=OUTPUT/'web/index.html'
    if not web.is_file():errors.append('Missing HTML edition')
    else:
        soup=BeautifulSoup(web.read_text(),'html.parser');ids={t['id'] for t in soup.find_all(id=True)}
        if soup.html.get('lang')!='de-DE':errors.append('HTML missing German language')
        if len(soup.find_all('nav'))<1:errors.append('HTML missing navigation')
        for img in soup.find_all('img'):
            if not img.get('alt','').strip():errors.append('HTML missing alt')
            if not img.get('src','').startswith('data:'):errors.append('HTML image not self-contained')
        for a in soup.find_all('a',href=True):
            href=a['href']
            if href.startswith('#') and unquote(href[1:]) not in ids:errors.append('HTML broken anchor '+href)
            elif not href.startswith(('#','http:','https:','mailto:')):
                target=web.parent/urlsplit(href).path
                if not target.exists():errors.append('HTML broken local link '+href)
        checks.append({'check':'html_navigation_and_images','headings':len(soup.find_all(re.compile('^h[1-6]$'))),'images':len(soup.find_all('img'))})
    result={'status':'passed' if not errors else 'failed','errors':errors,'checks':checks,'unique_referenced_images':len(images),'caption_instances':captions,'limitations':['Checks detect structural failures; they do not establish instructional correctness or legal accessibility compliance.']}
    (ROOT/'quality/assets_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False,indent=2));return not errors

if __name__=='__main__':sys.exit(0 if validate() else 1)
