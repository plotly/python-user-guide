
readme:
	less make_instructions.txt

publish:
	ipython nbconvert --to html s*/*.ipynb
	ipython scripts/translate_href-html.py *.html
	ipython scripts/publish.py *.html
	rm *.html

# templates to .ipynb
run:
	add templates ..
	ipython run ...
	
run-all:
	nbs=$(find ...)
	for nb in nbs:
		run ${nb}

# .ipynb to HTML ready to be djangoed
#
publish:
	ipython nbconvert --to html $1
	ipython scripts/translate_links.py $1   (translate.json) --> in run
	ipython scripts/get_body-head.py $1 
	ipython scripts/move_to_tree.py $1   (tree.json)
	
	(rm .html, get /tree/branch/branch/{head.txt,body.txt)
	

publish-all:
	nbs=$(find ...)
	for nb in nbs:
		publish ${nb}

push-to-sb:

	cp -R published/api-docs/ ../streambed/shelly/api_docs/templates/api_docs/user-guide/


