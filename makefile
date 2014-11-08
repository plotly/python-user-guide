# --- python-user-guide/ makefile ---

# Set (relative or absolute) path to streambed
streambed_path="../streambed"

# List of notebooks paths to be used in the plot.ly User Guide
ug-nbs = s*/*.ipynb

# -------------------------------------------------------------------------------

instructions:
	@cat Contributing.md | less

run-all:
	@scripts/nb_execute-all.sh

convert: $(ug-nbs)
	@ipython nbconvert --to html $(ug-nbs)
	@mv *.html converted/

publish:
	@rm -f publish.log
	@ipython scripts/publish.py converted/*.html

push-to-streambed:
	@rm -rf $(streambed_path)/shelly/templates/api_docs/includes/user_guide/python/*
	@rm -rf $(streambed_path)/shelly/api_docs/static/api_docs/image/user_guide/python/*
	@cp -R published/includes/* $(streambed_path)/shelly/templates/api_docs/includes/user_guide/python/
	@cp -R published/static/image/* $(streambed_path)/shelly/api_docs/static/api_docs/image/user_guide/python/
	@cp published/python_urls.py $(streambed_path)/shelly/api_docs/urls/user_guide/
	@cp published/python_sitemaps.py $(streambed_path)/shelly/api_docs/sitemaps/user_guide/

link-nbs-to-plotly: $(ug-nbs)
	@ipython scripts/translate_href-ipynb.py $(ug-nbs)

clean-converted:
	rm -f converted/*

clean-published:
	rm -rf published/*

clean: clean-converted clean-published
