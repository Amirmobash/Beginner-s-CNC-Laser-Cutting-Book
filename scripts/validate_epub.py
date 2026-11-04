#!/usr/bin/env python3
"""Check archive, metadata, reading order, resources, navigation; run EPUBCheck."""
import json,os,posixpath,shutil,subprocess,sys,zipfile
from pathlib import Path
from urllib.parse import urlsplit,unquote
from lxml import etree
from book_common import ROOT,OUTPUT


def validate(path=None):
    path=Path(path) if path else OUTPUT/'CNC_Laser_Geschenkbox.epub'
    errors=[];checks=[];external={'status':'unrun','reason':'EPUBCheck executable/JAR not available'}
    try:
        with zipfile.ZipFile(path) as z:
            names=set(z.namelist());first=z.infolist()[0]
            if first.filename!='mimetype' or first.compress_type!=zipfile.ZIP_STORED or z.read('mimetype')!=b'application/epub+zip':errors.append('Invalid EPUB mimetype placement/content/compression')
            container=etree.fromstring(z.read('META-INF/container.xml'))
            opfpath=container.find('.//{*}rootfile').get('full-path');opf=etree.fromstring(z.read(opfpath));base=posixpath.dirname(opfpath)
            if opf.get('version')!='3.0':errors.append('EPUB version is not 3.0')
            for tag in ['title','creator','identifier','language']:
                el=opf.find('.//{http://purl.org/dc/elements/1.1/}'+tag)
                if el is None or not (el.text or '').strip():errors.append('Missing metadata '+tag)
            lang=opf.find('.//{http://purl.org/dc/elements/1.1/}language')
            if lang is not None and lang.text!='de-DE':errors.append('Unexpected publication language')
            manifest={el.get('id'):el for el in opf.findall('.//{*}manifest/{*}item')}
            spine=opf.findall('.//{*}spine/{*}itemref')
            if len(spine)<11:errors.append('Missing manuscript sections in reading order')
            nav=[];xml_docs={};images=0
            for identity,item in manifest.items():
                dest=posixpath.normpath(posixpath.join(base,unquote(item.get('href'))))
                if dest not in names:errors.append('Manifest target missing '+dest);continue
                if 'nav' in item.get('properties','').split():nav.append(dest)
                if item.get('media-type')=='application/xhtml+xml':
                    try:xml_docs[dest]=etree.fromstring(z.read(dest))
                    except etree.XMLSyntaxError as e:errors.append('Malformed XHTML '+dest+': '+str(e))
                elif item.get('media-type','').startswith('image/'):images+=1
            if len(nav)!=1:errors.append('EPUB must have exactly one navigation document')
            for item in spine:
                if item.get('idref') not in manifest:errors.append('Broken spine idref')
            for name,doc in xml_docs.items():
                if doc.get('{http://www.w3.org/XML/1998/namespace}lang')!='de-DE':errors.append('Missing document language '+name)
                for img in doc.findall('.//{*}img'):
                    if not img.get('alt','').strip():errors.append('Missing alt '+name)
                for el in doc.iter():
                    for attr in ['src','href']:
                        ref=el.get(attr)
                        if not ref or urlsplit(ref).scheme:continue
                        parsed=urlsplit(ref);target=posixpath.normpath(posixpath.join(posixpath.dirname(name),unquote(parsed.path))) if parsed.path else name
                        if target not in names:errors.append('Broken EPUB reference '+name+' → '+ref)
                        elif parsed.fragment and target in xml_docs and not xml_docs[target].xpath('//*[@id=$id]',id=unquote(parsed.fragment)):errors.append('Broken EPUB anchor '+ref)
            if images<30:errors.append('Too few embedded images')
            checks=[{'check':'epub_structure','spine_sections':len(spine),'manifest_items':len(manifest),'xhtml_documents':len(xml_docs),'images':images}]
    except Exception as e:errors.append(type(e).__name__+': '+str(e))
    command=None
    jar=os.environ.get('EPUBCHECK_JAR','/workspace/book-tools/epubcheck-5.4.0/epubcheck.jar')
    if Path(jar).is_file():command=['java','-jar',jar,str(path)]
    elif shutil.which('epubcheck'):command=['epubcheck',str(path)]
    if command:
        run=subprocess.run(command,text=True,capture_output=True)
        external={'status':'passed' if run.returncode==0 else 'failed','exit_code':run.returncode,'stdout':run.stdout,'stderr':run.stderr}
        if run.returncode:errors.append('EPUBCheck failed')
    result={'status':'passed' if not errors else 'failed','errors':errors,'checks':checks,'epubcheck':external,'limitations':['EPUB structure/EPUBCheck are not a legal accessibility assessment or a reading-system compatibility test.']}
    (ROOT/'quality/epub_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False,indent=2));return not errors

if __name__=='__main__':sys.exit(0 if validate(sys.argv[1] if len(sys.argv)>1 else None) else 1)
