#!/usr/bin/env python3
"""Rebuild unchanged editorial inputs and compare artifact bytes with the prior build."""
import json,subprocess,sys
from pathlib import Path
from book_common import ROOT,OUTPUT,sha,sources


def main():
    names=['CNC_Laser_Geschenkbox_Digital.pdf','CNC_Laser_Geschenkbox_Amir_Mobasheraghdam.docx','CNC_Laser_Geschenkbox.epub','reader_project_files.zip','web/index.html','COVER.jpg']
    inputs=list(sources())+[p for folder in ['figures','cover','engineering','scripts'] for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts]
    before_inputs={str(p.relative_to(ROOT)):sha(p) for p in inputs}
    before={name:sha(OUTPUT/name) for name in names}
    run=subprocess.run([sys.executable,str(ROOT/'scripts/build_book.py')],cwd=ROOT,text=True,capture_output=True)
    after={name:sha(OUTPUT/name) for name in names}
    after_inputs={str(p.relative_to(ROOT)):sha(p) for p in inputs}
    stable=before_inputs==after_inputs
    comparisons={name:{'before':before[name],'after':after[name],'identical':before[name]==after[name]} for name in names}
    result={'status':'passed' if run.returncode==0 and stable and all(x['identical'] for x in comparisons.values()) else 'failed','build_exit_code':run.returncode,'inputs_unchanged':stable,'compared_artifacts':comparisons,'build_stderr':run.stderr,'scope':'Repeat build in the prepared local environment; no claim of restoration from a fresh remote clone.'}
    (ROOT/'quality/reproducibility.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    if result['status']=='passed':
        metrics_path=ROOT/'quality/build_metrics.json'
        metrics=json.loads(metrics_path.read_text());metrics['reproducibility']='Byte-identical repeated local build verified for all six artifacts.'
        metrics_path.write_text(json.dumps(metrics,ensure_ascii=False,indent=2))
    print(json.dumps(result,ensure_ascii=False,indent=2));return result['status']=='passed'

if __name__=='__main__':sys.exit(0 if main() else 1)
