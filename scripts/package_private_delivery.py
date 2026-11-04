#!/usr/bin/env python3
"""Create a local-only commercial delivery archive; never upload or stage it."""
from pathlib import Path
import hashlib,json,zipfile
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/CNC_Laser_Geschenkbox_Produktionspaket.zip'
EXCLUDED={'__pycache__','.git','.venv','.cache','evidence','renders','screenshots','ace','build'}
TOP=['README.md','AGENTS.md','BOOK_BIBLE.md','PROJECT_STATE.md','requirements.txt','.gitignore','manuscript','engineering','figures','cover','assets','scripts','research','publishing','quality','output']
def main():
    files=[]
    for name in TOP:
        path=ROOT/name
        candidates=path.rglob('*') if path.is_dir() else [path]
        for p in candidates:
            if p.is_file() and p!=OUT and not EXCLUDED.intersection(p.relative_to(ROOT).parts):files.append(p)
    manifest={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(set(files))}
    with zipfile.ZipFile(OUT,'w',zipfile.ZIP_DEFLATED) as z:
        for name in sorted(manifest):
            zi=zipfile.ZipInfo(name,(2026,11,4,12,0,0));zi.compress_type=zipfile.ZIP_DEFLATED;zi.external_attr=0o644<<16;z.writestr(zi,(ROOT/name).read_bytes())
        zi=zipfile.ZipInfo('DELIVERY_MANIFEST.json',(2026,11,4,12,0,0));zi.compress_type=zipfile.ZIP_DEFLATED
        z.writestr(zi,json.dumps(manifest,ensure_ascii=False,indent=2))
    with zipfile.ZipFile(OUT) as z:
        assert z.testzip() is None
        for name,digest in manifest.items():assert hashlib.sha256(z.read(name)).hexdigest()==digest
    print(json.dumps({'archive':str(OUT.relative_to(ROOT)),'files':len(manifest),'bytes':OUT.stat().st_size,'integrity':'passed'},indent=2))
if __name__=='__main__':main()
