# Federico De Santi, CV

Personal CV based on this [template](https://github.com/dgerosa/CV) made by Davide Gerosa.

- [**Full CV**](https://github.com/dgerosa/CV/releases/latest/download/FedericoDeSanti_fullCV.pdf)
- [**Short CV**](https://github.com/dgerosa/CV/releases/latest/download/FedericoDeSanti_shortCV.pdf)
- [**Publication list**](https://github.com/dgerosa/CV/releases/latest/download/FedericoDeSanti_publist.pdf)
- [**Talk list**](https://github.com/dgerosa/CV/releases/latest/download/FedericoDeSanti_talklist.pdf)

## How to use  
The only files one needs to change are `database.py` and `CV.tex`. Everything else is machine-generated.

- Add new papers and talks in `database.py` in the same format as the others. The order is important (recent first).
- Touch the other things in the CV directly in `CV.tex`.

The magic happes in `makeCV.py`. In particular:
- Fetch citations from [ADS](https://ui.adsabs.harvard.edu/search/q=orcid%3A0009-0000-2445-5729&sort=date%20desc%2C%20bibcode%20desc&p_=0) and [INSPIRE](https://inspirehep.net/authors/2851558?ui-citation-summary=true).
- Put together a papers and talks list in tex format (`parsepapers.tex`  and `parsetalks.tex`).
- Compute some basic indicators like h-index, etc (`metricspapers.tex`  and `metricstalks.tex`).
- Fetch bibtex record from  [ADS](https://ui.adsabs.harvard.edu/search/q=author%3A%22De%20Santi%2C%20Federico%22&sort=date%20desc%2C%20bibcode%20desc&p_=0) (`publist.bib `).
- Sanitize the database if the ADS key changed.
- Build the full CV with publication and presentation lists (`CV.tex`).
- Build a shorter CV without lists (`CVshort.tex`). This is done using the tags `%mark_CVshort`  in `CV.tex`.
- Build a standalone publication list (`publist.tex`).
- Build a standalone presentation list (`talklist.tex`).
- Push all of this to this [git](https://github.com/fdesanti/CV) repository.
- (*TODO*) Publish [releases](https://github.com/fdesanti/CV/releases) to get permanent URLs.


After changes, just type in shell

```shell
python makeCV.py --commit "commit messsage" --git
```

the "--git" options pushes to the repository and creates the release.
You can omit if you just want to recompile the pdflatex