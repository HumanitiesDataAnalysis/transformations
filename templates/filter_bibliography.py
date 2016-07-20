#! /usr/bin/python
import re
import glob

# Bibliography entries to retrieve
# Multiple pattern compilation from: http://stackoverflow.com/a/11693340/147021

markdowns = glob.glob("*.md")  + glob.glob("*/*.md") + glob.glob("*/*/*.md")

matches = set([])
for file in markdowns:
    for line in open(file):
        citations = re.search(r"@([A-Za-z0-9_][A-Za-z0-9_:\.#$%&-\+\?<>~]+[A-Za-z0-9_])",line)
        if citations:
            for match in citations.groups():
                matches.add(match)


with open('../../MyLibrary.bib', 'r') as bib_file:
    keep_printing = False
    for line in bib_file:
        is_key = re.search(r"^@\w+\{(.*),",line)
        if is_key:
            key=is_key.groups()[0]
            if key in matches:
                keep_printing = True

        if line.strip() == '}':
            if keep_printing:
                print line
                # End of an entry -- should be the one which began earlier
                keep_printing = False

        if keep_printing:
            # The intermediate lines
            print line,
