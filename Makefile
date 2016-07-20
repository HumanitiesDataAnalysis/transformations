
pandocOptions=--template=templates/template.tex --latex-engine=xelatex --bibliography=works_cited.bib --smart --csl=templates/inline.csl

PDFS1=$(patsubst %.md,%.pdf,$(shell find transformations -iname '*.md' | sed 's/ /\\ /g'))

PDFS=$(subst transformations/,pdfs/,$(PDFS1))


#works_cited.bib: ../../MyLibrary.bib
#	python templates/filter_bibliography.py > $@

all: $(PDFS)
	echo $(PDFS)

pdfs/%.pdf: transformations/%.md
	echo "Building with base format"
	pandoc -o $@ $(pandocOptions) $<

pdfs/Word_Embeddings.pdf: transformations/Word_Embeddings.md
	pandoc -o $@ $(pandocOptions) $<
