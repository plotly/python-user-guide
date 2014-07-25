
run-all:
	scripts/nb_execute-all.sh


publish:
	ipython nbconvert --to html s*/*.ipynb
	ipython scripts/translate_href-html.py *.html
	ipython scripts/publish.py *.html
	rm *.html

push-to-streambed:
	cp -R published/user-guide/python/* ../streambed/shelly/api_docs/templates/api_docs/user-guide/python
