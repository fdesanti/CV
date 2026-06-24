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
 
    # papers['submitted']['data'].append({
    #    "title":    "Inferring the population properties of galactic binaries from LISA's stochastic foreground",
    #    "author":   "F. De Santi, A. Santini, A. Toubiana, N. Karnesis, D. Gerosa",
    #    "journal":  "(2026)",
    #    "link":     "",
    #    "arxiv":    "arXiv:2602.18560 [astro-ph.HE]",
    #    "ads":      "2026arXiv260218560D",
    #    "inspire":  "DeSanti:2026xhs",
    #    "more":     ""
    #    })


if published:
    papers['published'] = {}
    papers['published']['label'] = 'Papers in major peer-reviewed journals'
    papers['published']['data'] = []

    papers['published']['data'].append({
        "title":    "Inferring the population properties of galactic binaries from LISA's stochastic foreground",
        "author":   "F. De Santi, A. Santini, A. Toubiana, N. Karnesis, D. Gerosa",
        "journal":  "\prd 113 (2026) 123006",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/9lc5-vgw5",
        "arxiv":    "arXiv:2602.18560 [astro-ph.HE]",
        "ads":      "2026PhRvD.113l3006D",
        "inspire":  "DeSanti:2026xhs",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Can Transformers help us perform parameter estimation of overlapping signals in gravitational wave detectors?",
        "author":   "L. Papalini, F. De Santi, M. Razzano, I. S. Heng, E. Cuoco",
        "journal":  "\cqg 42, 185012 (2025)",
        "link":     "https://iopscience.iop.org/article/10.1088/1361-6382/adfd33",
        "arxiv":    "arXiv:2505.02773 [gr-qc]",
        "ads":      "2025CQGra..42r5012P",
        "inspire":  "Papalini:2025exy",
        "more":     ""
        })

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
        "title":    "New strategies for seismic attenuation at low frequency for third generation gravitational waves detectors",
        "author":   "M. Vacatello, S. Ardito, M. Baratti, G. Bartoli, L. Bellizzi, G. Demasi, F. De Santi, F. Fidecaro, A. Fiori, L. Muccillo, M.A. Palaia, L. Papalini, M. Razzano",
        "journal":  "Nuovo Cim.C 48 (2025) 3, 106",
        "link":     "https://www.sif.it/riviste/sif/ncc/econtents/2025/048/03/article/30",
        "arxiv":    "",
        "ads":      "",
        "inspire":  "Vacatello:2025lvc",
        "more":     ""
        })
    
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
        "journal":  "JCAP 03 (2026) 081",
        "link":     "https://iopscience.iop.org/article/10.1088/1475-7516/2026/03/081",
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
        "title":    "What Lies Beneath the Noise: Inferring Galactic Binary Populations in LISA with SBI",
        "where":    "\href{https://indico.cern.ch/event/1640502/}{AI for Gravitational Waves Workshop} - CERN (Geneve)",
        "when":     "5-8 May 2026",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Inferring the Population properties of Galactic binaries from LISA'S stochastic foreground",
        "where":    "\href{https://sites.google.com/unimib.it/gwfreeride/}{GWFreeride 2026} - Sexten (Italy)",
        "when":     "26-30 January 2026",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Inferring the Population properties of Galactic binaries from LISA'S stochastic foreground",
        "where":    "\href{https://agenda.infn.it/event/49512/}{TEONGRAV Workshop 2026} - Pisa (Italy)",
        "when":     "14-16 January 2026",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Inferring Population properties of galactic binaries with Simulation Based Inference",
        "where":    "\href{https://www.astro.unige.ch/people/melanie.habouzit/LISA2025/index.php}{LISA AstroWG Meeting} - Geneve (Switzerland)",
        "when":     "16-18 December 2025",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Inferring Population properties of Galactic binaries from the Confusion Noise with SBI",
        "where":    "\href{https://sites.google.com/unimib.it/sigrav2025/home?authuser=0}{SIGRAV 2025} - Milan (Italy)",
        "when":     "8-12 September 2025",
        "invited":  False,
        "more":     ""
        })
    
    talks['conferences']['data'].append({
        "title":    "Inferring Population Properties of Galactic Binaries in LISA with Simulation Based Inference",
        "where":    "\href{https://iop.eventsair.com/gr24-amaldi16/}{GR/Amaldi 2025} - Glasgow (Scotland)",
        "when":     "14-18 July 2025",
        "invited":  False,
        "more":     ""
        })
    
    talks['conferences']['data'].append({
        "title":    "Transformers plus Normalizing Flows for parameter estimation of overlapping gravitational waves in next-generation detectors",
        "where":    "\href{https://agenda.infn.it/event/43565/overview/}{EuCAIFCon 2025} - Cagliari, Italy",
        "when":     "16-20 June 2025",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Inferring Population Properties of Galactic Binaries in LISA with Simulation Based Inference",
        "where":    "\href{https://uofgravity.github.io/aislands/}{AIslands 2025} - Rothesay, Isle of Bute (Scotland)",
        "when":     "13-15 May 2025",
        "invited":  False,
        "more":     ""
        })
    
    talks['conferences']['data'].append({
        "title":    "Machine Learning and Simulation Based Inference for ET \& LISA",
        "where":    "\href{https://davidegerosa.com/thuram/}{THURAM 2025} - GSSI, L'Aquila (Italy)",
        "when":     "7-9 May 2025",
        "invited":  True,
        "more":     ""
        })
    
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
        "title":    "Population Inference of Galactic binaries from LISA's stochastic foreground",
        "where":    "\href{https://indico.global/event/16100/timetable/?view=standard}{BiCoQ Poster Festival 2025}",
        "when":     "9 Dec. 2025",
        "link":     "https://indico.global/event/16100/timetable/?view=standard",
        "invited":  False,
        "more":     ""
        })

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
