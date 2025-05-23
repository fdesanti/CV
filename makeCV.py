import os
import sys
import time
import html
import json
import shutil
import gspread
import requests
import argparse
import warnings
import numpy as np
import urllib.error
import urllib.request
#import ads
#import copy
#import skywalker

from tqdm import tqdm
from datetime import datetime
from scholarly import scholarly
from database import papers, talks
#from github_release import gh_release_create

#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

def hindex(citations):
    return sum(x >= i + 1 for i, x in enumerate(sorted(  list(citations), reverse=True)))

def roundto100(N):
    return int(N/100)*100

def pdflatex(filename):
    os.system('pdflatex '+filename+' >/dev/null')
'''
def checkinternet():
    url = "http://www.google.com"
    timeout = 5
    connected = True
    try:
	    requests.get(url, timeout=timeout)
    except (requests.ConnectionError, requests.Timeout) as exception:
	    connected = False
    return connected
'''

def ads_citations(papers,testing=False):

    print('Get citations from ADS')

    token = os.getenv("ADS_TOKEN")  # if passed via env
        
    if token is None:
        with open('/Users/fdesanti/tokens/adstoken.txt') as f:
            #ads.config.token = f.read()
            token = f.read()

    tot = len(np.concatenate([papers[k]['data'] for k in papers]))
    with tqdm(total=tot) as pbar:
        for k in papers:
            for p in papers[k]['data']:
                if p['ads']:
                    if testing:
                        p['ads_citations'] = np.random.randint(0, 100)
                        p['ads_found'] = p['ads']
                    else:
                        n_retries=0
                        
                        p['ads_citations'] = 0
                        p['ads_found'] = ""
                        
                        while n_retries<10:
                            try:
                                with warnings.catch_warnings():
                                    warnings.filterwarnings("ignore", message="Unverified HTTPS request is being made to host")
                                    r = requests.get("https://api.adsabs.harvard.edu/v1/search/query?q="+p['ads'].replace("&","%26")+"&fl=citation_count,bibcode",headers={'Authorization': 'Bearer ' + token},verify=False)
                                q= r.json()['response']['docs']
                                #print(p['ads'], q)
                                if len(q)!=1:
                                    raise ValueError("ADS error in "+b)
                                q=q[0]
                                if q['citation_count'] is not None:
                                    p['ads_citations'] = q['citation_count']
                                else:
                                    print("Warning: citation count is None.", p['ads'])
                                    p['ads_citations'] = 0
                                p['ads_found'] = q['bibcode']

                            except Exception as e:
                                print(e)
                                retry_time = 5 #req.getheaders()["retry-in"]
                                print('ADS API error: retry in', retry_time, 's. -- '+p['ads'])
                                time.sleep(retry_time)
                                n_retries = n_retries + 1
                            
                                if n_retries==11:
                                    print('ADS API error: giving up -- '+p['ads'])

                                    #raise ValueError("ADS error in "+p['ads'])
                                continue
                            else:
                                break

                else:
                    p['ads_citations'] = 0
                    p['ads_found'] = ""
                pbar.update(1)

    return papers


def inspire_citations(papers,testing=False):

    print('Get citations from INSPIRE')

    tot = len(np.concatenate([papers[k]['data'] for k in papers]))
    with tqdm(total=tot) as pbar:
        for k in papers:
            for p in papers[k]['data']:
                if p['inspire']:
                    if testing:
                        p['inspire_citations'] = np.random.randint(0, 100)
                    else:
                        n_retries=0
                        while n_retries<10:
                            try:
                                req = urllib.request.urlopen("https://inspirehep.net/api/literature?q=texkey:"+p['inspire'])
                            except urllib.error.HTTPError as e:
                                if e.code == 429:
                                    retry_time = 10 #req.getheaders()["retry-in"]
                                    print('INSPIRE API error: retry in', retry_time, 's. -- '+p['inspire'])
                                    time.sleep(retry_time)
                                    n_retries = n_retries + 1
                                    continue
                                else:
                                    raise ValueError("INSPIRE error in "+p['inspire'])
                            else:

                                q = json.loads(req.read().decode("utf-8"))
                                n = len(q['hits']['hits'])
                                if n!=1:
                                    raise ValueError("INSPIRE error in "+b)
                                p['inspire_citations']=q['hits']['hits'][0]['metadata']['citation_count']
                                break

                else:
                    p['inspire_citations'] = 0
                pbar.update(1)

    return papers

def google_scholar_citations(papers,testing=False):
    print('Get citations from Google Scholar')
    # Search for your author profile (replace "Your Name" with your real name)
    #author = next(scholarly.search_author("Federico De Santi Bicocca"))
    #author = scholarly.fill(author)
    MY_AUTHOR_ID = "O45Yt4AAAAAJ"  
    author = scholarly.fill(scholarly.search_author_id(MY_AUTHOR_ID))
    citations = []
    # Print citations for each paper
    for pub in tqdm(author['publications']):
        #print(f"{pub['bib']['title']}: {pub['num_citations']} citations")
        citations.append(np.float64(pub['num_citations']))
    return citations


def parsepapers(papers,filename="parsepapers.tex"):

    print('Parse papers from database')

    out=[]
    for k in ['submitted','published','proceedings', 'others']:
        i = len(papers[k]['data'])

        if i>=1:
            out.append("\\textcolor{color1}{\\textbf{"+papers[k]['label']+":}}")
        out.append("\\vspace{-0.5cm}")
        out.append("\phantom{phantom text}")
        out.append("")
        out.append("\cvitem{}{\small\hspace{-1cm}\\begin{longtable}{rp{0.3cm}p{15.8cm}}")
        out.append("%")

        for p in papers[k]['data']:
            out.append("\\textbf{"+str(i)+".} & & \\textit{"+p['title'].strip(".")+".}")
            out.append("\\newline{}")
            if "F. De Santi" in p['author']:
                out.append(p['author'].replace("F. De Santi","\\textbf{F. De Santi}").strip(".")+".")
            else:
                out.append(p['author'].strip(".")+".")
            out.append("\\newline{}")
            line=""
            if p['link']:
                line +="\href{"+p['link']+"}"
            if p['journal']:
                line+="{"+p['journal'].strip(".")+"}. "
            if 'erratum' in p.keys():
                if p['errlink']:
                    line +="\href{"+p['errlink']+"}"
                if p['erratum']:
                    line+="{Erratum: "+p['erratum'].strip(".")+"}. "
            if p['arxiv']:
                line+="\href{https://arxiv.org/abs/"+p['arxiv'].split(":")[1].split(" ")[0]+"}{"+p['arxiv'].strip(".")+".}"
            out.append(line)
            if p['more']:
                out.append("\\newline{}")
                out.append("\\textcolor{color1}{$\\bullet$} "+p['more'].strip(".")+".")
            out.append("\\vspace{0.09cm}\\\\")
            out.append("%")
            i=i-1
        out.append("\end{longtable} }")

    with open(filename,"w") as f: f.write("\n".join(out))


def parsetalks(talks,filename="parsetalks.tex"):

    print('Parse talks from database')

    out=[]
    out.append("Invited talks marked with *.")
    out.append("\\vspace{0.2cm}")
    out.append("")

    for k in ['conferences','seminars','lectures','posters','outreach']:
        if len(talks[k]['data'])>=1:
            out.append("\\textcolor{color1}{\\textbf{"+talks[k]['label']+":}}")
            out.append("\\vspace{-0.5cm}")
            out.append("")
            out.append("\cvitem{}{\small\hspace{-1cm}\\begin{longtable}{rp{0.3cm}p{15.8cm}}")
            out.append("%")

            i = len(talks[k]['data'])
            for p in talks[k]['data']:
                if p["invited"]:
                    mark="*"
                else:
                    mark=""
                out.append("\\textbf{"+str(i)+".} & "+mark+" & \\textbf{"+p['title'].strip(".")+".}")
                out.append("\\newline{}")
                out.append("\\textit{" + p['where'].strip(".")+"}, "+p['when'].strip(".")+".")
                if p['more']:
                    out.append("\\newline{}")
                    out.append("\\textcolor{color1}{$\\bullet$} "+p['more'].strip(".")+".")
                out.append("\\vspace{0.05cm}\\\\")
                out.append("%")
                i=i-1
            out.append("\end{longtable} }")

    with open(filename,"w") as f: f.write("\n".join(out))


def metricspapers(papers,filename="metricspapers.tex"):

    print('Compute papers metrics')

    out=[]
    out.append("\cvitem{}{\\begin{tabular}{rcl}")
    out.append("\\textcolor{mark_color}{\\textbf{Publications}}: &\hspace{0.3cm} &")
    out.append("\\textbf{"+str(len(papers['published']['data']))+"} papers published in major peer-reviewed journals,")
    if len(papers['submitted']['data'])>1:
        out.append("\\textbf{"+str(len(papers['submitted']['data']))+"} papers in submission stage,")
    elif len(papers['submitted']['data'])==1:
        out.append("\\textbf{"+str(len(papers['submitted']['data']))+"} paper in submission stage,")

    out.append("\\\\ & &")
    out.append("\\textbf{"+str(len(papers['proceedings']['data']))+"} other publications (white papers, long-authorlist reviews, proceedings, software, etc)")
    out.append("\\\\ & &")

    first_author = []
    for k in ['submitted','published','proceedings']:
        for p in papers[k]['data']:
            if "F. De Santi" not in p['author']:
                raise ValueError("Looks like you're not an author:", p['title'])
            first_author.append( p['author'].split("F. De Santi")[0]=="" )

    out.append("(out of which \\textbf{"+str(np.sum(first_author))+"} first-authored papers")

    press_release = []
    for k in ['submitted','published','proceedings', 'others']:
        for p in papers[k]['data']:
            press_release.append("press release" in p['more'])
    if np.sum(press_release)>0:
        out.append(" and \\textbf{"+str(np.sum(press_release))+"} papers covered by press releases")
    out.append(").")
    out.append("\end{tabular} }\medskip")

    # including long-authorlist
    ads_citations     = np.concatenate([[p['ads_citations'] for p in papers[k]['data']] for k in papers])
    inspire_citations = np.concatenate([[p['inspire_citations'] for p in papers[k]['data']] for k in papers])
    scholar_citations = np.array(google_scholar_citations(papers))
    max_citations_including = np.array([cit.max() for cit in [ads_citations, inspire_citations, scholar_citations]])
    totalnumber_including = max([cit.sum() for cit in [ads_citations, inspire_citations, scholar_citations]])
    hind_including = hindex(max_citations_including)

    # excluding long-authorlist
    ads_citations = np.concatenate([[p['ads_citations'] for p in papers[k]['data']] for k in ['submitted','published']])
    inspire_citations = np.concatenate([[p['inspire_citations'] for p in papers[k]['data']] for k in ['submitted','published']])
    scholar_citations = np.array(google_scholar_citations(papers))
    max_citations_excluding = np.array([cit.max() for cit in [ads_citations, inspire_citations, scholar_citations]])
    totalnumber_excluding = max([cit.sum() for cit in [ads_citations, inspire_citations, scholar_citations]])
    hind_excluding = hindex(max_citations_excluding)

    print("\tTotal number of citations:", totalnumber_including, totalnumber_excluding)
    print("\th-index:", hind_including, hind_excluding)
    out.append("Summary metrics reported using ADS and InSpire excluding [including] long-authorlist papers:")
    out.append("\\\\\medskip")
    #out.append("\\textcolor{mark_color}{\\textbf{Total number of citations}}: >"+str(roundto100(totalnumber_excluding))+" [>"+str(roundto100(totalnumber_including))+"]")
    out.append("\\textcolor{mark_color}{\\textbf{Total number of citations}}: "+str(int(totalnumber_excluding))+" ["+str(int(totalnumber_including))+"].")

    out.append(" --- ")
    out.append("\\textcolor{mark_color}{\\textbf{h-index}}: "+str(hind_excluding)+" ["+str(hind_including)+"].")
    out.append("\\\\\medskip")  
    out.append("\\textcolor{mark_color}{\\textbf{Web links to list services}}:")
    out.append("\href{https://ui.adsabs.harvard.edu/search/q=orcid%3A0009-0000-2445-5729&sort=date+desc}{\\textsc{ADS}};")
    out.append("\href{https://inspirehep.net/literature?sort=mostrecent&size=25&page=1&q=a%20F.De.Santi.2}{\\textsc{InSpire}};")
    out.append("\href{https://scholar.google.com/citations?user=DCKKPBoAAAAJ&hl=it}{\\textsc{Google Scholar}};")
    out.append("\href{https://arxiv.org/a/desanti_f_1.html}{\\textsc{arXiv}};")
    out.append("\href{https://orcid.org/0009-0000-2445-5729}{\\textsc{ORCID}}.")

    with open(filename,"w") as f: f.write("\n".join(out))


def metricstalks(talks,filename="metricstalks.tex"):

    print('Compute talks metrics')


    out=[]
    out.append("\cvitem{}{\\begin{tabular}{rcl}")
    out.append("\\textcolor{mark_color}{\\textbf{Presentations}}: &\hspace{0.3cm} &")
    out.append("\\textbf{"+str(len(talks['conferences']['data']))+"} talks at conferences,")
    out.append("\\textbf{"+str(len(talks['seminars']['data']))+"} talks at department seminars,")
    out.append("\\textbf{"+str(len(talks['posters']['data']))+"} posters at conferences,")
    out.append("\\\\ & &")

    invited = []
    for k in ['conferences','seminars','posters']:
        for p in talks[k]['data']:
            invited.append(p['invited'])

    plural = "s" if len(talks['lectures']['data'])>1 else ""

    out.append("(out of which \\textbf{"+str(np.sum(invited))+"} invited presentations),")
    
    if len(talks['lectures']['data'])>0:
        out.append("\\textbf{"+str(len(talks['lectures']['data']))+"} lecture"+plural+" at PhD schools,")
    if len(talks['outreach']['data'])>0:
        out.append("\\textbf{"+str(len(talks['outreach']['data']))+"} outreach talks.")

    out.append("\end{tabular} }")

    with open(filename,"w") as f: f.write("\n".join(out))


def convertjournal(j):
    journalconversion                                                                              = {}
    journalconversion['\prd']                                                                      = ["Physical Review D", "PRD"]
    journalconversion['\prdrc']                                                                    = ["Physical Review D", "PRD"]
    journalconversion['\prdl']                                                                     = ["Physical Review D", "PRD"]
    journalconversion['\prl']                                                                      = ["Physical Review Letters","PRL"]
    journalconversion['\prr']                                                                      = ["Physical Review Research","PRR"]
    journalconversion['\mnras']                                                                    = ["Monthly Notices of the Royal Astronomical Society","MNRAS"]
    journalconversion['\mnrasl']                                                                   = ["Monthly Notices of the Royal Astronomical Society","MNRAS"]
    journalconversion['\cqg']                                                                      = ["Classical and Quantum Gravity","CQG"]
    journalconversion['\\aap']                                                                     = ["Astronomy & Astrophysics","A&A"]
    journalconversion['\\apj']                                                                     = ["Astrophysical Journal","APJ"]
    journalconversion['\\apjl']                                                                    = ["Astrophysical Journal","APJ"]
    journalconversion['\grg']                                                                      = ["General Relativity and Gravitation","GRG"]
    journalconversion['\lrr']                                                                      = ["Living Reviews in Relativity","LRR"]
    journalconversion['\\natastro']                                                                = ["Nature Astronomy","NatAstro"]
    journalconversion['Proceedings of the International Astronomical Union']                       = ["IAU Proceedigs","IAU"]
    journalconversion['Journal of Physics: Conference Series']                                     = ["Journal of Physics: Conference Series","JoPCS"]
    journalconversion['Journal of Open Source Software']                                           = ["Journal of Open Source Software","JOSS"]
    journalconversion['Astrophysics and Space Science Proceedings']                                = ["Astrophysics and Space Science Proceedings","AaSSP"]
    journalconversion['Caltech Undergraduate Research Journal']                                    = ["Caltech Undergraduate Research Journal","CURJ"]
    journalconversion['Chapter in: Handbook of Gravitational Wave Astronomy, Springer, Singapore'] = ['Book contribution','book']
    journalconversion['Rendiconti Lincei. Scienze Fisiche e Naturali']                             = ['Rendiconti Lincei','Lincei']
    journalconversion['Proceedings of the 57th Rencontres de Moriond']                             = ['Moriond proceedings','Moriond']
    journalconversion["arXiv e-prints"]                                                            = ["arXiv","arXiv"]
    journalconversion["Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment"] = ["Nuclear Instruments and Methods in Physics Research Section A","JNIMA"]

    if j in journalconversion:
        return journalconversion[j]
    else:
        return [j,j]


def citationspreadsheet(papers):

    gc = gspread.service_account()
    sh = gc.open("Citation count")

    print('Write Google Spreadsheet: List')

    spreaddata={}
    spreaddata['first_author']=[]
    spreaddata['ads_citations']=[]
    spreaddata['inspire_citations']=[]
    spreaddata['max_citations']=[]
    spreaddata['title']=[]
    spreaddata['journal']=[]
    spreaddata['year']=[]
    spreaddata['arxiv']=[]

    for k in papers:
        for p in papers[k]['data']:
            spreaddata['first_author'].append(p['author'].split(",")[0].split(".")[-1].strip().replace("\`",""))
            spreaddata['ads_citations'].append(p['ads_citations'])
            spreaddata['inspire_citations'].append(p['inspire_citations'])
            spreaddata['max_citations'].append(max(p['ads_citations'],p['inspire_citations']))
            spreaddata['title'].append(p['title'])
            if p['journal']:
                spreaddata['journal'].append(p['journal'].split("(")[0].replace("in press","").rstrip(" 0123456789.,") )
            elif p['arxiv']:
                spreaddata['journal'].append('arXiv')
            else:
                spreaddata['journal'].append("")
            if p['journal'] == "PhD thesis":
                spreaddata['year'].append(2016)
            elif p['journal'] and "(" in  p['journal'] and ")" in  p['journal']:
                spreaddata['year'].append(p['journal'].split("(")[-1].split(")")[0])
            elif p['arxiv']:
                spreaddata['year'].append("20"+p['arxiv'].split(':')[1][:2])
            else:
                spreaddata['year'].append()
            if p['arxiv']:
                spreaddata['arxiv'].append(p['arxiv'].split(']')[0].split("[")[1])
            else:
                spreaddata['arxiv'].append("None")
    tot = len(spreaddata['title'])
    for x in spreaddata:
        assert(len(spreaddata[x]) == tot)

    ind = np.argsort(spreaddata['max_citations'])[::-1]
    for x in spreaddata:
        spreaddata[x]=np.array(spreaddata[x])[ind]

    worksheet = sh.worksheet("List")
    worksheet.update("A3",np.expand_dims(np.arange(tot)+1,1).tolist())
    worksheet.update("C3",np.expand_dims(spreaddata['first_author'],1).tolist())
    worksheet.update("D3",np.expand_dims(spreaddata['year'],1).tolist())
    worksheet.update("E3",np.expand_dims(spreaddata['title'],1).tolist())
    worksheet.update("F3",np.expand_dims(spreaddata['ads_citations'],1).tolist())
    worksheet.update("G3",np.expand_dims(spreaddata['inspire_citations'],1).tolist())
    worksheet.update("H3",np.expand_dims(spreaddata['max_citations'],1).tolist())
    worksheet.update("F2",str(np.sum(spreaddata['ads_citations'])))
    worksheet.update("G2",str(np.sum(spreaddata['inspire_citations'])))
    worksheet.update("H2",str(np.sum(spreaddata['max_citations'])))
    worksheet.update("I2",str(hindex(spreaddata['max_citations'])))

    print('Write Google Spreadsheet: Year')

    singleyear=np.array(list(set(spreaddata['year'])))
    journalcount = np.array([np.sum(spreaddata['year']==s) for s in singleyear])
    ind = np.argsort(singleyear)
    singleyear=singleyear[ind]
    journalcount=journalcount[ind]

    worksheet = sh.worksheet("Years")
    worksheet.update("A2",np.expand_dims(np.array(singleyear),1).tolist())
    worksheet.update("B2",np.expand_dims(np.array(journalcount),1).tolist())

    print('Write Google Spreadsheet: Journals')

    shortpub = [convertjournal(j)[1] for j in spreaddata['journal']]
    singlepub = np.array([convertjournal(j)[1] for j in list(set(shortpub))])
    journalcount = np.array([np.sum(np.array([convertjournal(j)[1] for j in shortpub])==s) for s in singlepub])

    ind = np.argsort(journalcount)[::-1]
    singlepub=singlepub[ind]
    journalcount=journalcount[ind]

    longjournals=[]
    for s in singlepub:
        for j in list(set(spreaddata['journal'])):
            if convertjournal(j)[1]==s:
                longjournals.append(convertjournal(j)[0])
                break
    # longpub=[]
    # shortpub=[]
    # for j in singlepub:
    #     if j in journalconversion:
    #         longpub.append(journalconversion[j][0])
    #         shortpub.append(journalconversion[j][1])
    #     else:
    #         longpub.append(j)
    #         shortpub.append(j)

    worksheet = sh.worksheet("Journals")
    worksheet.update("A2",np.expand_dims(np.array(longjournals),1).tolist())
    worksheet.update("B2",np.expand_dims(np.array(journalcount),1).tolist())
    worksheet.update("D2",np.expand_dims(np.array(singlepub),1).tolist())


    print('Write Google Spreadsheet: arXiv')

    singlearxiv=np.array(list(set(spreaddata['arxiv'])))
    # Remove empty
    singlearxiv=singlearxiv[singlearxiv!=""]
    journalcount = np.array([np.sum(spreaddata['arxiv']==s) for s in singlearxiv])

    ind = np.argsort(journalcount)[::-1]
    singlearxiv=singlearxiv[ind]
    journalcount=journalcount[ind]

    worksheet = sh.worksheet("arXiv")
    worksheet.update("A2",np.expand_dims(np.array(singlearxiv),1).tolist())
    worksheet.update("B2",np.expand_dims(np.array(journalcount),1).tolist())


def builddocs():

    print("Update CV")
    pdflatex("CV")

    print("Update publist")
    pdflatex("publist")

    print("Update talklist")
    pdflatex("talklist")

    print("Update CVshort")
    with open('CV.tex', 'r') as f:
        CV = f.read()
    CVshort = "%".join(CV.split("%mark_CVshort")[::2])
    with open('CVshort.tex', 'w') as f:
        f.write(CVshort)
    pdflatex("CVshort")


def buildbib():

    print("Build bib file from ADS")

    with open('publist.bib', 'r') as f:
        publist = f.read()

    stored = []
    for p in publist.split('@'):
        if "BibDesk" not in p:
            stored.append(p.split("{")[1].split(",")[0])

    tot = len(np.concatenate([papers[k]['data'] for k in papers]))
    with tqdm(total=tot) as pbar:
        for k in papers:
            for p in papers[k]['data']:

                if  p['ads_found'] and p['ads_found'] not in stored:
                    with urllib.request.urlopen("https://ui.adsabs.harvard.edu/abs/"+p['ads_found']+"/exportcitation") as f:
                        bib = f.read()
                    bib=bib.decode()
                    bib = "@"+list(filter(lambda x:'adsnote' in x, bib.split("@")))[0].split("</textarea>")[0]
                    bib=html.unescape(bib)

                    if "journal =" in bib:
                        j  = bib.split("journal =")[1].split("}")[0].split("{")[1]
                        bib = bib.replace(j,convertjournal(j)[0])

                    with open('publist.bib', 'a') as f:
                        f.write(bib)
                pbar.update(1)

def replacekeys():

    print("Checking ADS keys")

    with open('database.py', 'r') as f:
        database = f.read()

    with open('publist.bib', 'r') as f:
        publist = f.read()

    for k in (papers):
        for p in (papers[k]['data']):

            #if p['ads']== "2021ApJ...915...56G":
            #    p['ads'] = "2021arXiv210411247G"

            if p['ads'] != p['ads_found'] and p['ads_found'] not in ["","None"]:

                print("\tReplace:", p['ads'],"-->", p['ads_found'])

                # Update in database
                database = database.replace(p['ads'],p['ads_found'])
                # Remove from bib file
                publist = "@".join([b for b in publist.split("@") if p['ads'] not in b])


    with open('database.py', 'w') as f:
        f.write(database)

    with open('publist.bib', 'w') as f:
        f.write(publist)


def pushtogit(comment=None):
    if comment is None:
        comment = "Generic update"

    print("Push to git:", comment)
    print(" ")
    os.system("git add -u")
    os.system("git commit -m '"+comment+"'")
    os.system("git push")

# def publishgithub():
#     date = datetime.now().strftime("%Y-%m-%d-%H-%M")
#     print("Publish github release:", date)

#     shutil.copy2("CV.pdf", "FedericoDeSanti_fullCV.pdf")
#     shutil.copy2("CVshort.pdf", "FedericoDeSanti_shortCV.pdf")
#     shutil.copy2("publist.pdf", "FedericoDeSanti_publist.pdf")
#     shutil.copy2("publist.bib", "FedericoDeSanti_publist.bib")
#     shutil.copy2("talklist.pdf", "FedericoDeSanti_talklist.pdf")

#     # Create a github token, see:
#     # https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
#     # Make sure a GITHUB_TOKEN variable is part of the environment variables

#     gh_release_create("fdesanti/CV", date, publish=True, name=date, asset_pattern="FedericoDeSanti_*")

#     os.system("git pull") # This is to get new tags from github


def clean():
    os.system("rm *.aux *.log *.out")


#####################################


if __name__ == "__main__":

    pars = argparse.ArgumentParser(description='Update CV')
    pars.add_argument('--connected', default=True, action='store_true', help='Connected mode')
    pars.add_argument('--testing', default=False, action='store_true', help='Testing mode')
    pars.add_argument('--commit', default=None, type=str, help='Commit comment')
    pars.add_argument('--git', default=False, action='store_true', help='Publish to github')

    args      = pars.parse_args()
    connected = args.connected
    testing   = args.testing
    comment   = args.commit
    git       = args.git

    if testing:
        print("Connected mode:", connected)
        print("Testing mode:", testing)
        print("Comment:", comment)
        print("Publish to github:", git)

    if connected:
        # Set testing=True to avoid API limit
        papers = ads_citations(papers,testing=testing)
        papers = inspire_citations(papers,testing=testing)
        parsepapers(papers)
        parsetalks(talks)
        metricspapers(papers)
        metricstalks(talks)
        buildbib()
        #citationspreadsheet(papers)

    replacekeys()
    builddocs()

    os.makedirs("CV", exist_ok=True)

    shutil.copy2("CV.pdf", "CV/FedericoDeSanti_fullCV.pdf")
    shutil.copy2("CVshort.pdf", "CV/FedericoDeSanti_shortCV.pdf")
    shutil.copy2("publist.pdf", "CV/FedericoDeSanti_publist.pdf")
    shutil.copy2("publist.bib", "CV/FedericoDeSanti_publist.bib")
    shutil.copy2("talklist.pdf", "CV/FedericoDeSanti_talklist.pdf")

    if comment is not None:
        pushtogit(comment)

        try:
            os.system("python github_release.py")
        except:
            print("[ERROR]: cannot publish a github release")
            pass
    
    # if git and connected and not testing:
    #     try:
    #         publishgithub()
    #     except:
    #         print("[ERROR]: cannot publish a github release")
    #         pass

    clean()