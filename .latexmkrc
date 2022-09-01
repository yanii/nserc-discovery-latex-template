# @default = ('main.txt');
@default_excluded_files = ('glossary.tex', 'application-config.tex');
$pdflatex = "lualatex -synctex=-1 %O %S";
$pdf_mode = 1;
$preview_mode = 0;
$postscript_mode = $dvi_mode = 0;
