import numpy as np
import sys,os

import json

papers      = {}
submitted   = True
published   = True
proceedings = True
others      = True

talks       = {}
conferences = True
posters     = True
seminars    = True
lectures    = True
outreach    = True

if submitted:

    papers['submitted'] = {}
    papers['submitted']['label'] = 'Submitted papers'
    papers['submitted']['data'] = []
 
    #papers['submitted']['data'].append({
    #    "title":    "",
    #    "author":   "",
    #    "journal":  "",
    #    "link":     "",
    #    "arxiv":    "",
    #    "ads":      "",
    #    "inspire":  "",
    #    "more":     ""
    #    })


if published:
    papers['published'] = {}
    papers['published']['label'] = 'Papers in major peer-reviewed journals'
    papers['published']['data'] = []

    papers['published']['data'].append({
        "title":    "Deep learning to detect gravitational waves from binary close encounters: Fast parameter estimation using normalizing flows",
        "author":   "F. De Santi, M. Razzano, F. Fidecaro, L. Muccillo, L. Papalini, B. Patricelli",
        "journal":  "\prd 109 (2024) 102004",
        "link":     "http://dx.doi.org/10.1093/mnrasl/sls018",
        "arxiv":    "arXiv:2404.12028 [gr-qc]",
        "ads":      "2024PhRvD.109j2004D",
        "inspire":  "DeSanti:2024oap",
        "more":     ""
        })


if proceedings:
    papers['proceedings'] = {}
    papers['proceedings']['label'] = 'White papers, long-authorlist reviews, conference proceedings, software papers, etc.'
    papers['proceedings']['data'] = []


    papers['proceedings']['data'].append({
        "title":    "Seismic isolation systems for next-generation gravitational wave detectors",
        "author":   "M. Razzano, F. Spada, G. Balestri, A. Basti, L. Bellizzi, F. De Santi, F. Fidecaro, A. Fiori, F. Frasconi, A. Gennai, L. Lucchesi, L. Muccillo, L. Orsini, M. Antonietta Palaia, L. Papalini, F. Pilo, P. Prosperi, M. Vacatello",
        "journal":  "Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment",
        "link":     "https://www.sciencedirect.com/science/article/pii/S0168900224006016",
        "arxiv":    "",
        "ads":      "2024NIMPA106769675R",
        "inspire":  "Razzano:2024wci",
        "more":     ""
        })


if others:
    papers['others'] = {}
    papers['others']['label'] = ''
    papers['others']['data'] = []

    #papers['others']['data'].append({
    #    "title":    title,
    #    "author":   F. De Santi,
    #    "journal":  "Master Thesis",
    #    "link":     link,
    #    "arxiv":    "",
    #    "ads":      ads,
    #    "inspire":  inspire,
    #    "more":     ""
    #    })

if conferences:
    talks['conferences'] = {}
    talks['conferences']['label'] = 'Talks at conferences'
    talks['conferences']['data'] = []
    

    #talks['conferences']['data'].append({
    #    "title":    title,
    #    "where":    where,
    #    "when":     when,
    #    "invited":  False,
    #    "more":     ""
    #    })

if seminars:
    talks['seminars'] = {}
    talks['seminars']['label'] = 'Talks at department seminars'
    talks['seminars']['data'] = []

    #talks['seminars']['data'].append({
    #    "title":    title,
    #    "where":    where,
    #    "when":     when,
    #    "invited":  True,
    #    "more":     ""
    #    })

if lectures:
    talks['lectures'] = {}
    talks['lectures']['label'] = 'Lectures at PhD schools'
    talks['lectures']['data'] = []

    #talks['lectures']['data'].append({
    #    "title":    title,
    #    "where":    where,
    #    "when":     when,
    #    "invited":  True,
    #    "more":     ""
    #    })

if posters:
    talks['posters'] = {}
    talks['posters']['label'] = 'Posters at conferences'
    talks['posters']['data'] = []

    talks['posters']['data'].append({
        "title":    "HYPERION: a Normalizing Flow based pipeline for the rapid parameter estimation of eccentric Close Encounters",
        "where":    "GraSP24 - Gravity Shape Pisa 2024 Conference",
        "when":     "23-25 Oct 2024",
        "invited":  False,
        "more":     ""
        })
    
    talks['posters']['data'].append({
        "title":    "HYPERION: a Normalizing Flow based pipeline for the rapid parameter estimation of eccentric Close Encounters",
        "where":    "GraviGammaNu Workshop 2024 (Bari)",
        "when":     "9-11 Oct 2024",
        "invited":  False,
        "more":     ""
        })
    
    talks['posters']['data'].append({
        "title":    "HYPERION: a Normalizing Flow based pipeline for the rapid parameter estimation of eccentric Close Encounters",
        "where":    "GraviGammaNu Workshop 2024 (Bari)",
        "when":     "9-11 Oct 2024",
        "invited":  False,
        "more":     ""
        })


if outreach:
    talks['outreach'] = {}
    talks['outreach']['label'] = 'Outreach talks'
    talks['outreach']['data'] = []

    #talks['outreach']['data'].append({
    #    "title":    title,
    #    "where":    where,
    #    "when":     when,
    #    "invited":  True,
    #    "more":     ""
    #    })

    


#######################################
