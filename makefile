instructions:
	cat make_instructions.md

# List of notebooks paths to be used in the plot.ly User Guide
ug-nbs = s*/*.ipynb

run-all:
	scripts/nb_execute-all.sh

convert: $(ug-nbs)
	ipython nbconvert --to html $(ug-nbs)
	mv *.html converted/

publish:
	ipython scripts/translate_href-html.py converted/*.html
	ipython scripts/publish.py converted/*.html
	ipython scripts/make_config.py

push-to-streambed:
	cp -R published/* ../streambed/shelly/templates/api_docs/includes/user-guide/python/

link-nbs-to-plotly: $(ug-nbs)
	ipython scripts/translate_href-ipynb.py $(ug-nbs)

clean-converted:
	rm -f converted/*

clean-published:
	rm -rf published/*

clean: clean-converted clean-published
