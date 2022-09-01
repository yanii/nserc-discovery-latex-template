# Uses the pandoc filter for acronyms: https://gitlab.com/-/snippets/1880361
all: main.pdf main.txt main.rtf main.md main.rst main.odt main.docx main.html count
main.pdf: *.tex references.bib nserc-appendix.cls
	latexmk -pdf main.tex
main.txt: main.pdf
	pandoc  --bibliography=references.bib --csl=ieee.csl --citeproc -F pandoc-acronym-filter.py --lua-filter pagebreak.lua main.tex  -o main.txt
main.html: main.pdf
	pandoc  --bibliography=references.bib --csl=ieee.csl --citeproc -F pandoc-acronym-filter.py --lua-filter pagebreak.lua main.tex  -o main.html
main.odt: main.pdf
	pandoc  --bibliography=references.bib --csl=ieee.csl --citeproc -F pandoc-acronym-filter.py --lua-filter pagebreak.lua main.tex  -o main.odt
main.rtf: main.pdf
	pandoc  --bibliography=references.bib --csl=ieee.csl --citeproc -F pandoc-acronym-filter.py --lua-filter pagebreak.lua main.tex -t rtf -o main.rtf
main.rst: main.pdf
	pandoc  --bibliography=references.bib --csl=ieee.csl --citeproc -F pandoc-acronym-filter.py --lua-filter pagebreak.lua main.tex  -o main.rst
main.md: main.pdf
	pandoc  --bibliography=references.bib --csl=ieee.csl --citeproc -F pandoc-acronym-filter.py --lua-filter pagebreak.lua main.tex  -o main.md
main.docx: main.pdf
	pandoc  --bibliography=references.bib --csl=ieee.csl --citeproc -F pandoc-acronym-filter.py --lua-filter pagebreak.lua main.tex  -o main.docx
count: main.pdf
	./checkcharacounts.py
clean:
	rm -f main.txt main.rtf main.rst main.md main.pdf main.docx main.html *.run.xml
	latexmk -c