A XeLaTeX template for NSERC-style documents
==========================================

## Why XeLaTex?

You have to use XeLaTeX to use the exact font required by NSERC (i.e. the real TrueType Times New Roman font). If you and your reviewers are less fussy, you may get away with using the standard LaTeX times font.
## Requirements for Makefile

Included is a Makefile for Linux/OS X that *requires* `PanDoc`, `latexmk` and Python 3. The Makefile will compile the XeLaTeX project, convert the LaTeX output to HTML, DOC, PDF, RTF, etc. (to allow for better copying of the LaTeX output into the NSERC Research Portal Forms), and uses a script `checkcharacounts.py` to check the NSERC maximum character counts are not exceeded for each section.

**You do not have to use this Makefile**. You can also just compile with latexmk or XeLaTeX and biber directly on `main.tex`.

## Subfiles

Each of the individual sections of the NSERC Discovery Proposal are separated into independent files using the `subfiles` package to allow for easier individual editing, or combined compilation in `main.tex`. This is optional, and you could remove `subfiles` if you prefer/don't have the package.


## Citation Aliases for CCV Entries

Fill in the info in `application-config.tex` and write your proposal text in `proposal.tex`, and the relevant sections of the DG application in the individual `.tex` files listed in `main.tex`. Add references to references.bib, with the special case of references from your CCV profile, which should be added as demonstrated in the template bibtex, i.e. with the keyword "ccv". For example, if we create a bibtex entry for the first conference publication in our CCV, i.e. C1, and we want this to refer to bibtex entry `me2016`:
```
@INPROCEEDINGS{me2016,
  ...
  KEYWORDS={ccv},
  ...
}
```

You can then use "citealias" to cite these by defining the citealiases using the CCV citation command It's easiest to create aliases, as shown in main.tex:
```
% CCV Citation Aliases
% TODO: CCV references should be created as citation aliases of the bibtex entries here.
\defcitealias{me2016}{\ccvcitation{C1}}
```

You will then be able to reference the CCV bibliography entry using
`\citetalias{me2016}`

## Support/Any Issues
Note that I made up this class for my own personal use; I don't mind sharing it, but please don't contact me for support. I'm also not responsible if you are not awarded a grant due to any issues with this template. NSERC Discovery Grant requirements can change every year, and you should check the posted requirements the year you apply. Saying this, this template is what I used for my successful Discovery Grant application in 2021.

About the author
----------------

This template was created by [Yani Ioannou](https://yani.ai), Assistant Professor at the [University of Calgary](https//www.ucalgary.ca), forked from the template and based on the LaTeX class designed by [Sylvain Hallé](http://leduotang.ca/sylvain). Also used is the pagebreak Lua script distributed with PanDoc by Benct Philip Jonsson and Albert Krewinkel, which can be found [here](https://github.com/pandoc/lua-filters/blob/master/pagebreak/pagebreak.lua).
