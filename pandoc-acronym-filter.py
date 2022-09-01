#!/usr/bin/env python3
# From https://gitlab.com/-/snippets/1880361

import os
from panflute import *
import re
import sys
# import subprocess

acronyms_full = {}
acronyms = {}

refcounts = {}

def resolveAcronyms(elem, doc):
    if isinstance(elem, Span) and "acronym-label" in elem.attributes:
        label = elem.attributes["acronym-label"]

        if label in acronyms:
            # this is the case: "singular" in form and "long" in form:
            shortvalue = acronyms[label]
            longvalue = acronyms_full[label]
            value = ''
            
            form = elem.attributes["acronym-form"]
            if label in refcounts and "short" in form:
                if "singular" in form:
                    value = shortvalue
                else:
                    value = shortvalue + "s"
            elif "full" in form or "short" in form:
                # remember that label has been used
                if "short" in form:
                    refcounts[label] = True
                
                if "singular" in form:
                    value = longvalue + " (" + shortvalue + ")"
                else:
                    value = longvalue + "s (" + shortvalue + "s)"
            elif "abbrv" in form:
                if "singular" in form:
                    value = shortvalue
                else:
                    value = shortvalue + "s"
            
            # DEBUG: print(label, form, value, file=sys.stderr)

            return Span(Str(value))

def loadAcronyms():
    pattern = re.compile(r"\\newacronym(\[.*\])?\{(?P<label>[A-Za-z]+)\}\{(?P<shortvalue>[A-Za-z 0-9]+)\}\{(?P<longvalue>[A-Za-z 0-9\-]+)\}")
    
    d = os.path.dirname(__file__)
    # d = subprocess.run(['kpsewhich', '-var-value', 'TEXMFHOME'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    filename = os.path.join(d, 'glossary.tex')
    with open(filename, 'r', encoding='utf-8') as acronymsFile:
        for line in acronymsFile:
            match = pattern.match(line)
           
            if match:
                # DEBUG: print(match.group('label'), match.group('shortvalue'), match.group('longvalue'), file=sys.stderr)
                acronyms_full[match.group('label')] = match.group('longvalue')
                acronyms[match.group('label')] = match.group('shortvalue')

def main(doc=None):
    loadAcronyms()
    return run_filter(resolveAcronyms, doc=doc)


if __name__ == "__main__":
    main()
