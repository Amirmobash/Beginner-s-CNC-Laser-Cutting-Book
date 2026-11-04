#!/usr/bin/env python3
"""Check source-register identity, evidence hashes and manuscript citations offline."""
import hashlib,json,re,sys
from book_common import ROOT,sources

def main():
    errors=[];warnings=[]
    registry=json.loads((ROOT/'research/sources.json').read_text())
    if isinstance(registry,dict):registry=registry.get('sources',[])
    ids={s.get('id') for s in registry}
    citations=set()
    for path in sources():
        text=path.read_text()
        for group in re.findall(r'\[((?:S\d{2}[,; ]*)+)\]',text):citations.update(re.findall(r'S\d{2}',group))
    for c in citations:
        if c not in ids:errors.append('Unknown citation '+c)
    evidence=0
    for s in registry:
        url=s.get('url','')
        if not url.startswith(('https://','http://')):errors.append('Invalid source URL '+str(s.get('id')))
        p=ROOT/'research/evidence'/f'{s.get("id")}.txt'
        expected=s.get('sha256')
        if p.exists() and expected:
            actual=hashlib.sha256(p.read_bytes()).hexdigest()
            if actual!=expected:errors.append('Evidence hash changed '+str(s.get('id')))
            evidence+=1
        if s.get('status','').startswith('nicht'):warnings.append('Unretrieved source '+str(s.get('id')))
    result={'status':'passed' if not errors else 'failed','errors':errors,'warnings':warnings,'registered_sources':len(registry),'cited_source_ids':sorted(citations),'hash_verified_evidence':evidence,'limitations':['URL syntax and evidence integrity checked offline; current external availability, rights, and factual correctness require separate source review.']}
    (ROOT/'quality/references_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False,indent=2));return not errors

if __name__=='__main__':sys.exit(0 if main() else 1)
