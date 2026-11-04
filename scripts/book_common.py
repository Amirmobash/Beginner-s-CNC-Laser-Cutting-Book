"""Shared deterministic publication model. Does not contain the manuscript."""
from pathlib import Path
import re, hashlib, json
import markdown
from bs4 import BeautifulSoup
import yaml

ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/'output'
TITLE='CNC & Laser für Einsteiger: Deine erste Geschenkbox aus Holz'
SUBTITLE='Schritt für Schritt vom ersten Entwurf über den Laserschnitt bis zur persönlichen CNC-Gravur'
AUTHOR='Amir Mobasheraghdam'
EPOCH=1793793600
DATE='2026-11-04'
UUID='urn:uuid:9f42331d-854e-553b-ae70-ed4dc9016bfb'


def sources():
    result=[ROOT/'manuscript/frontmatter.md']+[ROOT/f'manuscript/chapter_{i:02}.md' for i in range(1,10)]+[ROOT/'manuscript/appendix.md', ROOT/'manuscript/bibliography.md']
    missing=[str(x.relative_to(ROOT)) for x in result if not x.is_file()]
    if missing: raise FileNotFoundError('Missing manuscript sources: '+', '.join(missing))
    return result


def metadata():
    p=ROOT/'manuscript/book_metadata.yaml'
    d=yaml.safe_load(p.read_text()) if p.exists() else {}
    return {'title':TITLE,'subtitle':SUBTITLE,'author':AUTHOR,'lang':'de-DE','date':DATE,**(d or {})}


def render_md(source):
    doc=markdown.markdown(source,extensions=['fenced_code','tables','attr_list','sane_lists'])
    soup=BeautifulSoup(doc,'html.parser')
    # Pandoc-style bracket source markers are intentional plain text citations.
    for table in soup.find_all('table'):
        if not table.find('thead'): continue
        for th in table.find('thead').find_all('th'): th['scope']='col'
    return str(soup)


def sections():
    result=[]
    for i,path in enumerate(sources()):
        html=render_md(path.read_text())
        soup=BeautifulSoup(html,'html.parser')
        used=set()
        for n,h in enumerate(soup.find_all(re.compile('^h[1-6]$'))):
            identity=f'{path.stem}-{n}'
            h['id']=identity;used.add(identity)
        # Caption text from Markdown image alt. Keep alt, add visible caption.
        for img in soup.find_all('img'):
            if img.parent.name=='figure': continue
            alt=img.get('alt','')
            fig=soup.new_tag('figure'); img.wrap(fig)
            caption=soup.new_tag('figcaption'); caption.string=alt;fig.append(caption)
            if fig.parent.name=='p': fig.parent.unwrap()
        first=soup.find(re.compile('^h[1-6]$'))
        result.append({'name':path.stem,'path':path,'html':str(soup),'title':first.get_text() if first else path.stem})
    return result


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
