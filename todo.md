
List of ideas for this project
------------------------------

* Change the font for the IPython notebook

`
from IPython.core.display import HTML

def css_styling():
    styles = open("../styles/custom.css", "r").read()
    return HTML(styles)
css_styling()
`
..* Some good-looking sans serif

..* IPython notebook CSS custom style!!!

* `Getting Started` should have:
..* a quick intro
..* the Plotly logo embedded

..* Table of Contents with links and full description 
    (including layout/style options covered, e.g. examples include )

..* Installation guidelines (info on api_key)
..* Sign up info --> Setup config.json as streaming demos!

..* Def function for embedding plotly graph in notebook! 
    Or not! Use p.iplot

..* Except the reader to be familiar with Python terminology (dictionaries,
object, numpy) ...

..* Contact info
..* Feedback!
..* mention that all files are available in a github repo!
..* links to similar documentation for R, Matlab, etc.


* 1 notebook for each of Plotly''s plot types

..* Line & Scatter Plots:
    a simple first plot, dictionaries/customization, file setting,
    plotly homepage

..* Bar Charts:
    find a good example on plot.ly (or wait for another section)

..* Subplots & Small Multiples
..* Error bars (attention to horizontal error bars)
..* Histograms
..* Box plots
..* Heatmaps & color scales (use your function for polar_vortex)
..* Bubble charts (use Jack''s example!!)
..* 2d Histograms
..* Polar Charts (coming soon)
..* Streaming Data
..* Retrieve Data from Plotly
..* 3d Surface Plots (coming soon)
..* Maps (coming soon)

..* (maybe) an FAQ section
..* List of Plotly style options with links to examples (in different chapter)! 
    --> code that with ''grep''!!!
..*  Troubleshooting and debugging

..* Should I call them ''Chapters'' or something else??


* At the bottom of every page (excluding Getting Started) put link to other
chapters (maybe only ''prev'' and ''next'') --> code that!


* How to incorporate documentation on plot.ly/api/docs/:

..* Line and Scatter (s1)
..* Error Bars
..* Bubble Charts
..* Area plots
..* Box Plots
..* Heatmaps
..* Bar Charts
..* Histograms
..* Text Charts
..* Mixed Types
..* Time series

..* Multiple axes, Insets and Subplots

..* Layout: Axes, Legends(s1 and ), 
    Global Font, Annotations, IFrames, Sizing, Labels

..* File Settings: Privacy, File Sharing, Overwrite, Append, Extend, Setting
    Layout, File Naming, Setting Style, Formal Syntax.






