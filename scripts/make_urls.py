import json
import sys
import os

# -------------------------------------------------------------------------------
# 
# Script that makes a django urls file containing all the 
# (using ./inputs/translate.json)
#
# -------------------------------------------------------------------------------

NAME="make_urls"  # name of this script

# Get translate.json, to translate HTML file names to branch names
def get_translate():
    with open('./scripts/inputs/translate.json') as f:
        translate = json.load(f)
    return translate

# Get chapter names from translate.json
def get_chapters(translate):
    return translate.values()

# Get urls patterns
# N.B.: r'(?P<lang>python)/' is in streambed/shelly/api_docs/__init__.py
def get_urls(chapters):
    urls = []
    for chapter in chapters:
        urls += [r'(?P<user_guide_chapter>{})/$'.format(chapter)]
    return urls

# Generate python_urls.py file
# See streambed/api_docs/ for more info
def get_urls_py(urls):
    urls_py = (
        "from django.conf.urls import patterns, url\n"
        "import api_docs.views\n\n"
        "urlpatterns = patterns(\n"
        "   '',\n"
    )
    for url in urls:
        urls_py += '    url("'+url+'", api_docs.views.user_guide_template)'
        if url != urls[-1]:
            urls_py += ",\n"
    urls_py += "\n)\n"
    return urls_py

# Replace python_urls.py
def replace_urls(urls_py):
    f_urls = "./published/python_urls.py"
    with open(f_urls, "w") as f:
        print "[{}]".format(NAME), '... writes in', f_urls
        f.write(urls_py)
    return

# -------------------------------------------------------------------------------

def main():

    translate = get_translate()
    chapters = get_chapters(translate)

    urls = get_urls(chapters)
    urls_py = get_urls_py(urls)

    replace_urls(urls_py)


if __name__ == "__main__":
    main()
