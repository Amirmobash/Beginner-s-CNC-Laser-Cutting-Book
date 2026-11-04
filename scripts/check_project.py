#!/usr/bin/env python3
"""Run required structural checks with real command return codes."""
import json,subprocess,sys,zipfile
from pathlib import Path
from book_common import ROOT,OUTPUT

def main():
    checks=[];errors=[]
    for script in ['validate_assets.py','validate_references.py','validate_epub.py']:
        r=subprocess.run([sys.executable,str(ROOT/'scripts'/script)],cwd=ROOT,text=True,capture_output=True)
        checks.append({'script':script,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
        if r.returncode:errors.append(script+' failed')
    archive=OUTPUT/'reader_project_files.zip'
    try:
        with zipfile.ZipFile(archive) as z:
            if z.testzip():errors.append('Reader ZIP CRC failure')
            names=z.namelist()
            if not any(x.endswith('.svg') for x in names):errors.append('Reader ZIP missing editable SVG')
            if not any(x.endswith('.json') for x in names):errors.append('Reader ZIP missing engineering specification')
            if any(n.startswith('/') or '..' in Path(n).parts for n in names):errors.append('Unsafe ZIP paths')
        checks.append({'archive_entries':len(names),'archive_crc':'passed'})
    except Exception as e:errors.append('Reader ZIP '+str(e))
    result={'status':'passed' if not errors else 'failed','errors':errors,'checks':checks}
    (ROOT/'quality/project_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False,indent=2));return not errors

if __name__=='__main__':sys.exit(0 if main() else 1)
