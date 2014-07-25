from bs4 import BeautifulSoup
import json
import sys

# -------------------------------------------------------------------------------
# 
# Script that strip ...
#
# -------------------------------------------------------------------------------

NAME="strip-html"  # file name

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

# Replace href to 
def replace_title_href(soup):
    old = "#"+soup.h1['id']
    new = "#notebook"
    for a in soup.findAll('a'):
        if a['href']==old:
            print "[{}]".format(NAME), '... link to title found:', a['href']
            a['href'] = a['href'].replace(old, new)
            print "[{}]".format(NAME), '... link updated to:', a['href']
    return soup

# Strip title (i.e. the first h1) tag from body
def strip_title(soup):
    soup.h1.extract()
    print "[{}]".format(NAME), '... strip title'
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

    for file_html in files_html:
        soup = get_soup(file_html)
        soup = replace_title_href(soup)
        soup = strip_title(soup)
        replace_file_html(soup, file_html)


if __name__ == "__main__":
    main()
