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
	ipython scripts/make_urls.py
	ipython scripts/make_sitemaps.py

push-to-streambed:
	cp -R published/includes/* ../streambed/shelly/templates/api_docs/includes/user_guide/python/
	cp published/python_urls.py ../streambed/shelly/api_docs/urls/user_guide/
	cp published/python_sitemaps.py ../streambed/shelly/api_docs/sitemaps/user_guide/

link-nbs-to-plotly: $(ug-nbs)
	ipython scripts/translate_href-ipynb.py $(ug-nbs)

clean-converted:
	rm -f converted/*

clean-published:
	rm -rf published/*

clean: clean-converted clean-published
