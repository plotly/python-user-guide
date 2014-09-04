import json
import sys
import os

# -------------------------------------------------------------------------------
# 
# Script that makes a django sitemaps file containing all the user guide items
# (using ./inputs/translate.json)
#
# -------------------------------------------------------------------------------

NAME="make_sitemaps"  # name of this script
tab = "    "         # tab in space


# Get translate.json, to translate HTML file names to branch names
def get_translate():
    with open('./scripts/inputs/translate.json') as f:
        translate = json.load(f)
    return translate

# Get chapter names from translate.json
def get_chapters(translate):
    return translate.values()

# Get sitemaps items
# N.B. To be imported in 
def get_items(chapters):
    locations = []
    lmfiles = []
    for chapter in chapters:
        locations += ["'/python/{}/'".format(chapter)]
        lmfiles += [("os.path.join(\n{tab}{tab}{tab}{tab}"
            "settings.TOP_DIR, "
            "'shelly',\n{tab}{tab}{tab}{tab}"
            "'templates', "
            "'api_docs', "
            "'includes',\n{tab}{tab}{tab}{tab}"
            "'user_guide',\n{tab}{tab}{tab}{tab}"
            "'python',\n{tab}{tab}{tab}{tab}"
            "'{chapter}',\n{tab}{tab}{tab}{tab}"
            "'body.html')"
        ).format(chapter=chapter,tab=tab)]
    return locations, lmfiles

# Generate python_sitemaps.py file
# See streambed/api_docs/ for more info
def get_sitemaps_py(locations, lmfiles):
    sitemaps_py = (
        "import os\n\n"
        "from django.conf import settings\n\n\n"
        "def items():\n"
        "    items = [\n"
    )
    for location, lmfile in zip(locations,lmfiles):
        sitemaps_py += (
        "{tab}{tab}dict(\n"
        "{tab}{tab}{tab}location={location},\n"
        "{tab}{tab}{tab}lmfile={lmfile},\n"
        "{tab}{tab}{tab}priority=0.5\n"
        "{tab}{tab})"
        ).format(location=location,lmfile=lmfile,tab=tab)
        if location != locations[-1]:
            sitemaps_py += ",\n"
    sitemaps_py += (
        "\n{tab}]"
        "\n{tab}return items"
        "\n"
    ).format(tab=tab)
    return sitemaps_py

# Replace python_sitemaps.py
def replace_sitemaps(sitemaps_py):
    f_urls = "./published/python_sitemaps.py"
    with open(f_urls, "w") as f:
        print "[{}]".format(NAME), '... writes in', f_urls
        f.write(sitemaps_py)
    return

# -------------------------------------------------------------------------------

def main():

    translate = get_translate()
    chapters = get_chapters(translate)

    locations, lmfiles = get_items(chapters)
    sitemaps_py = get_sitemaps_py(locations, lmfiles)

    replace_sitemaps(sitemaps_py)


if __name__ == "__main__":
    main()
