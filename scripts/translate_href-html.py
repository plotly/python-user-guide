from bs4 import BeautifulSoup
import json
import sys

# -------------------------------------------------------------------------------
# 
# Script that converts inter-User Guide href in HTML NBs
# (using ./inputs/translate.json)
#
# -------------------------------------------------------------------------------

NAME="translate_href-html"  # file name

# Get input arguments 
def get_args():
    args = sys.argv[1:]
    if not args:
        print ("usage:\n"
               "python {NAME}.py file.html \n"
               "python {NAME}.py file1.html file2.html ...  fileN.html\n".format(NAME=NAME))
        sys.exit(0)
    else:
        return args

# Get HTML soup from HTML file path
def get_soup(file_html):
    with open(file_html, "r") as f:
        print "[{}]".format(NAME), 'Opening', file_html
        return BeautifulSoup(f)

# Get URLs of domains 
def get_domains():
    return dict(
        nbviewer="http://nbviewer.ipython.org/github/plotly/python-user-guide/blob/master/",
        plotly="/python/"  # main branch in Django
    )

# Get translate.json, to translate URL tails from 
# nbviewer to plot.ly domain
# (e.g. s00_homepage/s00_homepage.ipynb to home
def get_translate():
    with open('./scripts/inputs/translate.json') as f:
        translate = json.load(f)
    return translate

# Replace 'nbviewer'-domain hrefs to plot.ly
# and translate URL tails in HTML soup
def replace_href(soup, domains, translate):
    for a in soup.findAll('a'):
        if domains['nbviewer'] in a['href']:
            print "[{}]".format(NAME), '... link found:', a['href']
            a['href'] = a['href'].replace(domains['nbviewer'], domains['plotly'])
            for old, new in translate.items():
                if old in a['href']:
                    a['href'] = a['href'].replace(old, new)
                    break
            else:
                print "[{}]".format(NAME), '... URL tail not found in translate.json'
            print "[{}]".format(NAME), '... link updated to:', a['href']
    return soup

# Replace HTML file 
def replace_file_html(soup, file_html):
    new_html = soup.prettify("utf-8")
    with open(file_html, "wb") as f:
        print "[{}]".format(NAME), '... overwrites', file_html
        f.write(new_html)
        return

# -------------------------------------------------------------------------------

def main():

    files_html = get_args()
    domains = get_domains()
    translate = get_translate()

    for file_html in files_html:
        soup = get_soup(file_html)
        soup = replace_href(soup, domains, translate)
        replace_file_html(soup, file_html)


if __name__ == "__main__":
    main()
