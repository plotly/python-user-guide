import json
import sys
import os

# -------------------------------------------------------------------------------
# 
# Script that 
# 
# (*)  adds this template to the published/ tree (using ./inputs/translate.json)
#
# -------------------------------------------------------------------------------

NAME="make_config"  # name of this script

# Get translate.json, to translate HTML file names to branch names
# (e.g. s00_homepage/s00_homepage.html to home)
def get_translate():
    with open('./scripts/inputs/translate.json') as f:
        translate = json.load(f)
    return translate

# Get chapter names from translate.json
def get_chapters(translate):
    return translate.values()

# Get config dictionary
# config.name : breadcrumb header label
# config.tags.title : META title
# config.tags.meta_description : META description
def get_config(chapter):

    # Default
    config = dict(
        name=chapter.replace('-',' ').replace(' tutorial','').title(),
        tags=dict(
            title=chapter.replace('-',' ').title(),
            meta_description=(
                "A tutorial on how to make beautiful {} "
                "with plotly and Python or IPython."
            ).format(chapter.replace('-',' ').replace(' tutorial',''))
        )
    )

    # Exceptions
    if chapter == 'user-guide':
        config['name'] = "Home"
        config['tags']['title'] = 'Contents'
        config['tags']['meta_description'] = (
            'A User Guide for Plotly Python / IPython API Library'
        )
    if chapter == 'overview':
        config['tags']['meta_description'] = (
            'An overview of Plotly Python / IPython API Library'
        )
    if chapter == 'matplotlib-to-plotly-tutorial': 
        config['tags']['meta_description'] = (
            'A tutorial on how to convert matplotlib figure '
            'to beautiful plotly figures'
        )
    if chapter == 'streaming-tutorial': 
        config['tags']['meta_description'] = (
            'An overview of plotly streaming plots.'
        )
    if chapter == 'streaming-line-tutorial': 
        config['tags']['meta_description'] = (
            "A tutorial on how to make beautiful streaming line plots "
            "with plotly and Python or IPython."
        )
    if chapter == 'streaming-double-pendulum-tutorial': 
        config['tags']['meta_description'] = (
            'A tutorial on how to make a beautiful streaming plot '
            'of a never-ending double pendulum simulation '
            'with plotly and Python or IPython.'
        )
    if chapter == 'streaming-bubbles-tutorial':
        config['tags']['meta_description'] = (
            'A tutorial on how to make a beautiful streaming plot '
            'an animated bubble chart'
            'with plotly and Python or IPython.'
        )
    if chapter == 'python-tutorial':
        config['tags']['meta_description'] = (
            'A tutorial on python features used in the User Guide'
        )

    return config

# Replace config.json 
def replace_config(config, chapter):
    path = os.path.join("./published/", chapter)
    f_config = os.path.join(path,"config.json")
    with open(f_config, "w") as f:
        print "[{}]".format(NAME), '... writes in', f_config
        json.dump(config, f, indent=4)
    return

# -------------------------------------------------------------------------------

def main():

    translate = get_translate()
    chapters = get_chapters(translate)

    for chapter in chapters:
        config = get_config(chapter)
        replace_config(config, chapter)

if __name__ == "__main__":
    main()
