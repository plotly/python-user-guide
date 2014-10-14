from bs4 import BeautifulSoup
import json
import sys
import os

import translate_href_html
import update_body
import make_config
import make_urls
import make_sitemaps

# -------------------------------------------------------------------------------
#
# Script that gets the html notebooks up to publishable level
#
# -------------------------------------------------------------------------------

NAME = "publish"  # name of this script


# Get input arguments
def get_args():
    path = sys.argv[0]
    args = sys.argv[1:]
    if not args:
        print ("usage:\n"
               "python {NAME}.py file.html \n"
               "python {NAME}.py file1.html file2.html "
               "...  fileN.html\n".format(NAME=NAME))
        sys.exit(0)
    else:
        return args, path


# Get translate.json, to translate HTML file names to branch names
# (e.g. s00_homepage/s00_homepage.html to home)
def get_translate():
    with open('./scripts/inputs/translate.json') as f:
        translate = json.load(f)
    return translate


# Get URLs of domains from domains.json
def get_domains():
    with open("./scripts/inputs/domains.json") as f:
        domains = json.load(f)
    return domains

# -------------------------------------------------------------------------------


# Get HTML soup from HTML file path
def get_soup(file_html):
    with open(file_html, "r") as f:
        print "[{}]".format(NAME), 'Opening', file_html
        return BeautifulSoup(f)


# Get HTML <body>
def get_body(soup):
    print "[{}]".format(NAME), '... grabs <body>'
    return soup.body

# -------------------------------------------------------------------------------


# Get the directory tree for the body.html leaf
def get_tree(file_html, translate):
    branch = "published/includes/"
    file_html_base = os.path.basename(file_html)
    for old, leaf in translate.items():
        old_base = os.path.basename(old).replace('.ipynb', '.html')
        if old_base == file_html_base:
            return "{branch}{leaf}/".format(branch=branch, leaf=leaf)
    else:
        print "[{}]".format(NAME), '!!! URL tail not found in translate.json'


# Make directory tree
def make_tree(tree):
    if not os.path.exists(tree):
        print "[{}]".format(NAME), '... making', tree
        os.makedirs(tree)
    else:
        print "[{}]".format(NAME), '...', tree, 'already exists OK'


# Overwrite body.html
def overwrite(body, tree):
    f_body = os.path.join(tree, "body.html")
    with open(f_body, "wb") as f:
        print "[{}]".format(NAME), '... writes in', f_body
        body = body.prettify().encode('utf8')
        body = body.replace('<body>', '')
        body = body.replace('</body>', '')
        f.write(str(body))
    return

# -------------------------------------------------------------------------------


def main():

    files_html, path = get_args()
    translate = get_translate()
    domains = get_domains()

    for file_html in files_html:

        soup = get_soup(file_html)
        body = get_body(soup)

        body = update_body.update_body(body)
        body = translate_href_html.translate(body, domains, translate)

        tree = get_tree(file_html, translate)
        make_tree(tree)
        overwrite(body, tree)

    make_config.make_config(translate)
    make_urls.make_urls(translate)
    make_sitemaps.make_sitemaps(translate)


if __name__ == "__main__":
    main()
