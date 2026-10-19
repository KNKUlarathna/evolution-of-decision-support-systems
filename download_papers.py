#!/usr/bin/env python3
"""Download directly linked free scholarly PDFs from the catalog with retries.
Usage: python download_papers.py --priority 1
       python download_papers.py --all
The script only uses URLs already present in DSS_Evolution_Literature.json.
No login/paywall bypasses. Rate limits may require manual use of repository page.
"""
import argparse, csv, json, pathlib, re, time, urllib.request, urllib.error
ROOT=pathlib.Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--all',action='store_true',help='Download every entry with a PDF link (default).')
parser.add_argument('--priority',type=int,choices=[1,2,3],help='Download this priority only')
parser.add_argument('--timeout',type=int,default=30)
parser.add_argument('--retries',type=int,default=3)
args=parser.parse_args()
records=json.loads((ROOT/'DSS_Evolution_Literature.json').read_text(encoding='utf-8'))
chosen=[r for r in records if r['Free_PDF_URL'] and (args.priority is None or r['Priority']==args.priority)]
folder=ROOT/'DSS_PDFs';folder.mkdir(exist_ok=True)
report=[]
for j,r in enumerate(chosen,1):
    safe=re.sub(r'[^a-zA-Z0-9-]+','_',r['Title']).strip('_')[:68]
    category=re.sub(r'[^a-zA-Z0-9-]+','_',r['Category'])
    sub=folder/category;sub.mkdir(exist_ok=True)
    file=sub/(r['ID']+'_'+str(r['Year'])+'_'+safe+'.pdf')
    stat='FAILED';why=''
    if file.exists() and file.read_bytes()[:5]==b'%PDF-':
        stat='EXISTS';why='Already a valid PDF'
    else:
        for attempt in range(1,args.retries+1):
            try:
                req=urllib.request.Request(r['Free_PDF_URL'],headers={'User-Agent':'Mozilla/5.0 (Academic Research; scholarly document download)','Accept':'application/pdf,*/*'})
                with urllib.request.urlopen(req,timeout=args.timeout) as resp:
                    data=resp.read(50*1024*1024)
                if not data.lstrip()[:8].startswith(b'%PDF-'):
                    raise ValueError('Server returned HTML/non-PDF content; download may require browser login.')
                file.write_bytes(data);stat='DOWNLOADED';why=f'{len(data):,} bytes';break
            except Exception as e:
                why=str(e)[:250]
                if attempt<args.retries:time.sleep(3*attempt)
    print(f'[{j}/{len(chosen)}] {r["ID"]} {stat}: {r["Title"][:64]} — {why}')
    report.append({'ID':r['ID'],'Title':r['Title'],'Status':stat,'Message':why,'PDF_URL':r['Free_PDF_URL'],'Path':str(file) if stat in ('EXISTS','DOWNLOADED') else ''})
    time.sleep(0.5)
with (ROOT/'DSS_Download_Results.csv').open('w',encoding='utf-8-sig',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=['ID','Title','Status','Message','PDF_URL','Path']);wr.writeheader();wr.writerows(report)
print(f'\nProcessed {len(report)} links; report: DSS_Download_Results.csv')
