
run-all:
	scripts/nb_execute-all.sh

convert:
	ipython nbconvert --to html s*/*.ipynb
	mv *.html converted/

publish:
	ipython scripts/translate_href-html.py converted/*.html
	ipython scripts/publish.py converted/*.html

clean:
	rm -f converted/*

push-to-streambed:
	cp -R published/* ../streambed/shelly/api_docs/templates/api_docs/user-guide/python
