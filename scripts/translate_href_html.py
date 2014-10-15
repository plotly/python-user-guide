from bs4 import BeautifulSoup
import json
import sys

# -------------------------------------------------------------------------------
# 
# Script that converts inter-User Guide href in HTML NBs
# (using ./inputs/translate.json)
#
# -------------------------------------------------------------------------------

NAME = "translate_href-html"  # file name


# Replace 'nbviewer'-domain hrefs to plot.ly
# and translate URL tails in HTML soup
def replace_href(soup, domains, translate):
    for a in soup.findAll('a'):
        for domain in [domains['nbviewer'],domains['plotly-ext'],'./']:
            if a['href'].startswith(domain):
                print "[{}]".format(NAME), '... link to translate found:', a['href']
                a['href'] = a['href'].replace(domain, domains['plotly-int'])
                for old, new in translate.items():
                    if old in a['href']:
                        a['href'] = a['href'].replace(old, new)
                        break
                    elif new in a['href']:
                        break
                else:
                    print "[{}]".format(NAME), '!!! URL tail not found in translate.json'
                    print "[{}]".format(NAME), '!!! make sure the translated url exists'
                print "[{}]".format(NAME), '... link translated to:', a['href']
    return soup

# -------------------------------------------------------------------------------

def translate(soup, domains, translate):
    soup = replace_href(soup, domains, translate)
    return soup
