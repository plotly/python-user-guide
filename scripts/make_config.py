import json
import sys
import os

# -------------------------------------------------------------------------------
# 
# Script that makes a config file for each notebook and sends it
# to the published/ tree (using ./inputs/translate.json)
#
# -------------------------------------------------------------------------------

NAME = "make_config"  # name of this script


# Get chapter names from translate.json
def get_chapters(translate):
    return translate.values()


# Get config dictionary
# config.userguide_chapter_name : breadcrumb header label
# config.tags.title : META title
# config.tags.meta_description : META description
def get_config(chapter):

    # Shortcut capitalizing first letter of each word except 'and', 'to' 
    def titled(s):
        return s.title().replace('And',"and").replace('To','to')

    # Set base name (without '-')
    base = chapter.replace('-',' ')

    # Exceptions (base name)
    if chapter == 'heatmaps-contours-and-2dhistograms-tutorial':
        base = base.replace('heatmaps','heatmaps,').replace('2dhistograms','2D histograms')

    # Set fields
    name = base.capitalize().replace(' tutorial','')
    title = "{} | Python User Guide | plotly".format(titled(base))
    descrip = (
        "A tutorial on how to make beautiful {} "
        "with plotly and Python or IPython."
    ).format(base.replace(' tutorial',''))

    # Exceptions (fields)
    if chapter == 'user-guide':
        name = ""
        title = "Python User Guide | plotly"
        descrip = "A User Guide for Plotly and its Python API Library"
    if chapter == 'overview':
        title = "Overview of Plotly and its Python API Library"
        descrip = "An overview of plotly and its Python API Library"
    if chapter == 'matplotlib-to-plotly-tutorial': 
        title = "Convert Matplotlib Graphs to Plotly | Python User Guide | plotly" 
        descrip = (
            'A tutorial on how to convert matplotlib figures '
            'to beautiful plotly figures.'
        )
    if chapter == 'streaming-tutorial': 
        name = "Streaming plots"
        title = "Overview of Streaming Plots | Python User Guide | plotly" 
        descrip = (
            'An overview of plotly streaming plots '
            'with plotly and Python or IPython.'
        )
    if chapter == 'streaming-line-tutorial': 
        name = "Streaming plots"
        title = "Streaming Line Plots | Python User Guide | plotly" 
        descrip = (
            "A tutorial on how to make beautiful streaming line plots "
            "with plotly and Python or IPython."
        )
    if chapter == 'streaming-double-pendulum-tutorial': 
        name = "Streaming plots"
        title = "A Streaming Double Pendulum | Python User Guide | plotly" 
        descrip = (
            'A tutorial on how to make a beautiful streaming plot '
            'of a never-ending double pendulum simulation '
            'with plotly and Python or IPython.'
        )
    if chapter == 'streaming-bubbles-tutorial':
        name = "Streaming plots"
        title = "Streaming Bubble Charts | Python User Guide | plotly" 
        descrip = (
            'A tutorial on how to make a beautiful streaming plot '
            'of an animated bubble chart '
            'with plotly and Python or IPython.'
        )
    if chapter == 'python-tutorial':
        name = "Python basics"
        title = "Python Tutorial | plotly"
        descrip = (
            'A tutorial on Python features most used with plotly in the '
            'Python User Guide'
        )

    # Output
    config = dict(
        user_guide_chapter_name=name,
        tags=dict(title=title,meta_description=descrip)
    )

    return config


# Replace config.json 
def replace_config(config, chapter):
    path = os.path.join("./published/includes/", chapter)
    f_config = os.path.join(path,"config.json")
    with open(f_config, "w") as f:
        print "[{}]".format(NAME), '... writes in', f_config
        json.dump(config, f, indent=4)
        f.write("\n")
    return

# -------------------------------------------------------------------------------


def make_config(translate):

    chapters = get_chapters(translate)

    for chapter in chapters:
        config = get_config(chapter)
        replace_config(config, chapter)

if __name__ == "__main__":
    main()
