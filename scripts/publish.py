from bs4 import BeautifulSoup
import json
import sys
import os

# -------------------------------------------------------------------------------
# 
# Script that parses HTML files into a <body> and <head> templates 
# and add these templates to the published/ tree
#
# -------------------------------------------------------------------------------

NAME="publish"  # file name

# Get input arguments 
def get_args():
    path = sys.argv[0]
    args = sys.argv[1:]
    if not args:
        print ("usage:\n"
               "python {NAME}.py file.html \n"
               "python {NAME}.py file1.html file2.html ...  fileN.html\n".format(NAME=NAME))
        sys.exit(0)
    else:
        return args, path

# Get HTML soup from HTML file path
def get_soup(file_html):
    with open(file_html, "r") as f:
        print "[{}]".format(NAME), 'Opening', file_html
        return BeautifulSoup(f)

# Get HTML <body> and <head>
def get_body_head(soup):
    print "[{}]".format(NAME), '... parsed <body> and <head>'
    return soup.body, soup.head

# Get translate.json, to translate HTML file names to branch names
# (e.g. s00_homepage/s00_homepage.html to home)
def get_translate():
    with open('./scripts/inputs/translate.json') as f:
        translate = json.load(f)
    return translate

# Get the directory tree for body.txt and head.txt leaves
def get_tree(file_html, translate):
    branch="published/user-guide/python/"
    file_html_base = os.path.basename(file_html)
    for old, leaf in translate.items():
        old_base = os.path.basename(old).replace('.ipynb','.html')
        if old_base == file_html_base:
            return "{branch}{leaf}/".format(branch=branch,leaf=leaf)
    else:
        print "[{}]".format(NAME), '... URL tail not found in translate.json'

# Make directory tree
def make_tree(tree):
    if not os.path.exists(tree):
        print "[{}]".format(NAME), '... making', tree
        os.makedirs(tree)
    else:
        print "[{}]".format(NAME), '...', tree, 'already exists OK'

# Replace (body/head) txt templates
def replace_templates(body, head, tree):
    for temp, f_temp in zip([body, head],['body.txt','head.txt']):
        path_temp = os.path.join(tree, f_temp)
        with open(path_temp, "wb") as f:
            print "[{}]".format(NAME), '... writes in', f_temp
            f.write(str(temp))
    return

# -------------------------------------------------------------------------------

def main():

    files_html, path = get_args()
    translate = get_translate()

    for file_html in files_html:
        soup = get_soup(file_html)
        body, head = get_body_head(soup)
        tree = get_tree(file_html, translate)
        make_tree(tree)
        replace_templates(body, head, tree)


if __name__ == "__main__":
    main()
