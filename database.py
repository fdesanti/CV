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
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.109.102004",
        "arxiv":    "arXiv:2404.12028 [gr-qc]",
        "ads":      "2024PhRvD.109j2004D",
        "inspire":  "DeSanti:2024oap",
        "more":     ""
        })


if proceedings:
    papers['proceedings'] = {}
    #papers['proceedings']['label'] = 'White papers, long-authorlist reviews, conference proceedings, software papers, etc.'
    papers['proceedings']['label'] = 'Conference proceedings'
    papers['proceedings']['data'] = []


    papers['proceedings']['data'].append({
        "title":    "Seismic isolation systems for next-generation gravitational wave detectors",
        "author":   "M. Razzano, F. Spada, G. Balestri, A. Basti, L. Bellizzi, F. De Santi, F. Fidecaro, A. Fiori, F. Frasconi, A. Gennai, L. Lucchesi, L. Muccillo, L. Orsini, M. Antonietta Palaia, L. Papalini, F. Pilo, P. Prosperi, M. Vacatello",
        "journal":  "Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment (2024)",
        "link":     "https://www.sciencedirect.com/science/article/pii/S0168900224006016",
        "arxiv":    "",
        "ads":      "2024NIMPA106769675R",
        "inspire":  "Razzano:2024wci",
        "more":     ""
        })


if others:
    papers['others'] = {}
    papers['others']['label'] = 'Collaboration and long author-list papers'
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
    papers['others']['data'].append({
        "title":    "The Science of The Einstein Telescope",
        "author":   "A. Abac et al. and the Einstein Telescope Collaboration",
        "journal":  "(2025)",
        "link":     "https://arxiv.org/abs/2503.12263",
        "arxiv":    "arXiv:2503.12263 [gr-qc]",
        "ads":      "",
        "inspire":  "Abac:2025saz",
        "more":     ""
        })

if conferences:
    talks['conferences'] = {}
    talks['conferences']['label'] = 'Talks at conferences'
    talks['conferences']['data'] = []
    

    talks['conferences']['data'].append({
        "title":    "Deep learning to detect gravitational waves from binary close encounters: Fast parameter estimation with normalizing flows",
        "where":    "LIGO-Virgo-KAGRA (LVK) Collaboration Meeting (Baton Rouge, USA)",
        "when":     "11-14 Mar. 2024",
        "invited":  False,
        "more":     "(online)"
        })
    
    talks['conferences']['data'].append({
        "title":    "Deep learning to detect gravitational waves from binary close encounters: Fast parameter estimation with normalizing flows",
        "where":    "\href{https://indico.ego-gw.it/event/666/overview}{Integrated Activities for the High Energy Astrophysics Domain (AHEAD2020) Workshop} - European Gravitational Wave Observatory (EGO), Cascina",
        "when":     "4-5 Mar. 2024",
        "invited":  False,
        "more":     ""
        })
    
    talks['conferences']['data'].append({
        "title":    "GW from Binary Close Encounters: Analysis with Normalizing Flow",
        "where":    "Virgo Week - European Gravitational Wave Observatory (EGO), Cascina",
        "when":     "5-9 Feb. 2024",
        "invited":  False,
        "more":     ""
        })
    
    talks['conferences']['data'].append({
        "title":    "GW from Binary Close Encounters: Analysis with Normalizing Flow",
        "where":    "Burst (LVK) Collaboration Meeting",
        "when":     "20 Dec. 2023",
        "invited":  False,
        "more":     "online"
        })

if seminars:
    talks['seminars'] = {}
    talks['seminars']['label'] = 'Talks at department seminars'
    talks['seminars']['data'] = []

    talks['seminars']['data'].append({
        "title":    "Probabilistic Machine Learning for the study of burst sources",
        "where":    "Virgo Pisa Internal Workshop (INFN Pisa)",
        "when":     "22-23 May 2024",
        "invited":  True,
        "more":     ""
        })

if lectures:
    talks['lectures'] = {}
    talks['lectures']['label'] = 'Lectures at PhD schools'
    talks['lectures']['data'] = []

    #talks['lectures']['data'].append({
    #    "title":    "Probabilistic Machine Learning for the study of burst sources",
    #    "where":    "Virgo Pisa Internal Workshop (INFN Pisa)",
    #    "when":     "22-23 May 2024",
    #    "invited":  True,
    #    "more":     ""
    #    })

if posters:
    talks['posters'] = {}
    talks['posters']['label'] = 'Posters at conferences'
    talks['posters']['data'] = []

    talks['posters']['data'].append({
        "title":    "HYPERION: a Normalizing Flow based pipeline for the rapid parameter estimation of eccentric Close Encounters",
        "where":    "\href{https://agenda.infn.it/event/40101/overview}{GraSP24 - Gravity Shape Pisa 2024 Conference}",
        "when":     "23-25 Oct. 2024",
        "link":     "https://agenda.infn.it/event/40101/overview",
        "invited":  False,
        "more":     ""
        })
    
    talks['posters']['data'].append({
        "title":    "HYPERION: a Normalizing Flow based pipeline for the rapid parameter estimation of eccentric Close Encounters",
        "where":    "\href{https://agenda.infn.it/event/38056/overview}{V GraviGammaNu Workshop 2024} (Bari)",
        "when":     "9-11 Oct. 2024",
        "invited":  False,
        "more":     ""
        })
    
    talks['posters']['data'].append({
        "title":    "Gravitational Waves from Binary Close Encounters: Fast Parameter Estimation with Normalizing Flows",
        "where":    "LIGO-Virgo-KAGRA (LVK) Collaboration Meeting (Toyama, Japan)",
        "when":     "11-14 Sep. 2023",
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
