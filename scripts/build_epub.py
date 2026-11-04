#!/usr/bin/env python3
"""Create a deterministic reflowable EPUB 3 from the shared editorial model."""
from pathlib import Path
import json, re, zipfile, posixpath, html
from lxml import etree, html as lhtml
from bs4 import BeautifulSoup
from book_common import ROOT,OUTPUT,TITLE,SUBTITLE,AUTHOR,DATE,UUID,sections,metadata

EPUB=OUTPUT/'CNC_Laser_Geschenkbox.epub'
XHTML='http://www.w3.org/1999/xhtml'
EPUBNS='http://www.idpf.org/2007/ops'


def xhtml(title,body):
    head=f'<head><title>{html.escape(title)}</title><link rel="stylesheet" type="text/css" href="style.css"/></head>'
    doc=lhtml.fromstring(f'<html xmlns="{XHTML}" xmlns:epub="{EPUBNS}" lang="de-DE" xml:lang="de-DE">{head}<body>{body}</body></html>')
    # XML serialization guarantees properly closed img and br tags.
    return b'<?xml version="1.0" encoding="utf-8"?>\n'+etree.tostring(doc,encoding='utf-8',method='xml')


def build_epub():
    OUTPUT.mkdir(exist_ok=True)
    docs=sections(); resources={}; manifest=[]; spine=[]; files={}; bookid=metadata().get('identifier',UUID)
    for n,sec in enumerate(docs):
        soup=BeautifulSoup(sec['html'],'html.parser')
        for img in soup.find_all('img'):
            src=img.get('src','');p=(ROOT/src).resolve()
            if not p.is_relative_to(ROOT) or not p.is_file():raise FileNotFoundError(src)
            name='images/'+p.name
            if name in resources and resources[name]!=p:raise ValueError('Duplicate asset basename '+name)
            resources[name]=p;img['src']=name
        for a in soup.find_all('a',href=True):
            href=a['href']
            if href.endswith('.md') and not href.startswith(('https://','http://','mailto:')):
                target=Path(href).stem
                a['href']=target+'.xhtml'
        filename=sec['name']+'.xhtml';files[filename]=xhtml(sec['title'],str(soup))
        manifest.append(f'<item id="s{n}" href="{filename}" media-type="application/xhtml+xml"/>');spine.append(f'<itemref idref="s{n}"/>')
    cover=ROOT/'cover/export/COVER.jpg'
    if not cover.exists():
        covers=sorted((ROOT/'cover/export').glob('*.jpg'))
        cover=covers[0] if covers else None
    if cover:
        resources['images/cover.jpg']=cover
        manifest.append('<item id="cover-image" href="images/cover.jpg" media-type="image/jpeg" properties="cover-image"/>')
        files['cover.xhtml']=xhtml(TITLE,'<section epub:type="cover"><h1>'+html.escape(TITLE)+'</h1><img src="images/cover.jpg" alt="Originales Titelbild: Geschenkbox aus Holz, Laser und CNC-Fräse"/></section>')
        manifest.append('<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>');spine.insert(0,'<itemref idref="cover"/>')
    for i,(name,p) in enumerate(sorted(resources.items())):
        files[name]=p.read_bytes()
        if name=='images/cover.jpg':continue
        media={'.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.svg':'image/svg+xml'}[p.suffix.lower()]
        manifest.append(f'<item id="im{i}" href="{name}" media-type="{media}"/>')
    nav='<nav epub:type="toc" id="toc"><h1>Inhalt</h1><ol>'
    for sec in docs:nav+=f'<li><a href="{sec["name"]}.xhtml">{html.escape(sec["title"])}</a></li>'
    nav+='</ol></nav>'
    files['nav.xhtml']=xhtml('Inhaltsverzeichnis',nav)
    files['style.css']=(ROOT/'scripts/book.css').read_text().split('@page')[0].encode()
    manifest+=['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>','<item id="css" href="style.css" media-type="text/css"/>']
    opf=f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id" xml:lang="de-DE" prefix="schema: http://schema.org/">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="book-id">{html.escape(bookid)}</dc:identifier><dc:title>{html.escape(TITLE)}</dc:title><dc:description>{html.escape(SUBTITLE)}</dc:description><dc:creator>{AUTHOR}</dc:creator><dc:language>de-DE</dc:language><dc:date>{DATE}</dc:date>
<meta property="dcterms:modified">{DATE}T12:00:00Z</meta>
<meta property="schema:accessMode">textual</meta><meta property="schema:accessMode">visual</meta><meta property="schema:accessModeSufficient">textual</meta>
<meta property="schema:accessibilityFeature">alternativeText</meta><meta property="schema:accessibilityFeature">readingOrder</meta><meta property="schema:accessibilityFeature">structuralNavigation</meta><meta property="schema:accessibilityFeature">tableOfContents</meta>
<meta property="schema:accessibilityHazard">none</meta><meta property="schema:accessibilitySummary">Semantische Überschriften, Navigation und deutsche Bildbeschreibungen sind vorhanden. Nicht als barrierefrei zertifiziert; manuelle Prüfung mit assistiven Technologien steht aus.</meta>
</metadata><manifest>{''.join(manifest)}</manifest><spine>{''.join(spine)}</spine></package>'''
    files['package.opf']=opf.encode()
    container=b'''<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="EPUB/package.opf" media-type="application/oebps-package+xml"/></rootfiles></container>'''
    with zipfile.ZipFile(EPUB,'w') as z:
        def put(name,data,compress=zipfile.ZIP_DEFLATED):
            info=zipfile.ZipInfo(name,(2026,11,4,12,0,0));info.compress_type=compress;info.external_attr=0o644<<16;z.writestr(info,data)
        put('mimetype',b'application/epub+zip',zipfile.ZIP_STORED);put('META-INF/container.xml',container)
        for name,data in sorted(files.items()):put('EPUB/'+name,data)
    return EPUB

if __name__=='__main__':print(build_epub())
