
List of ideas for this project
------------------------------

* Change the font for the IPython notebook. Code OK,
  Look Some good-looking sans serif

* `Getting Started` should have:

+ a quick intro
+ the Plotly logo embedded

+ Table of Contents with links and full description 
    (including layout/style options covered, e.g. examples include )

+ Installation guidelines (info on api_key)
+ Sign up info --> Setup config.json as streaming demos!

+ What version of Plotly, Python, IPython is assumed?

+ Except the reader to be familiar with Python terminology (dictionaries,
object, numpy) ...

+ Contact info
+ Feedback!
+ mention that all files are available in a github repo!
+ links to similar documentation for R, Matlab, etc.


* 1 notebook for each of Plotly''s plot types

+ Line & Scatter Plots:
    a simple first plot, 
    dictionaries/customization (plot type, color, style, title, axis/legend
    labels), 
    file setting (file name, output, overwrite)
    plotly homepage (...)

+ Bar Charts and Error Bars: 
    find a good example/ dataset on plot.ly 
    attention to horizontal error bars
    tick label in text( Jan, Feb, ...)

    - fig 4: simple bar chart (T_avg and T_std, vertical montreal)
    - fig 5: Horizontal bar+ error_x (value) (P_avg, P_ext (stack) for vancouver)
    - fig 6: Montreal vs. Vancouver T_avg and P_avg (2-panels or multi-axes??)

    - Ask jack about Bar bottom, 
      look up github to nbviewer before, cleanup folder
    
+ Histogram, where?? Want to show how to make the Plotly logo??
    talk about 'barmode': 'stack' in here maybe?

+ Box Plots, where?? With Histogram??

+ Subplots & Small Multiples (Multiple Axes, Subplots, Insets)
    example a retrieving data from plot. with browser!
    Do a multiple axes in Bar Charts (i.e. Temp and Precip) ???

+ Error bars (now with Bar Charts)
+ Histograms (maybe with Bar Charts??)

+ Box plots
+ Heatmaps, 2d Histograms & color scales (use your function for polar_vortex)
+ Bubble charts (use Jack''s example!!)

+ 2d Histograms (with Heatmaps)
+ Polar Charts (coming soon)
+ Streaming Data
+ Retrieve Data from Plotly
+ 3d Surface Plots (coming soon)
+ Maps (coming soon)

+ (maybe) an FAQ section
+ List of Plotly style options with links to examples (in different chapter)! 
    --> code that with ''grep''!!!
+  Troubleshooting and debugging

+ Should I call them ''Chapters'' or something else??
+ Should I call put ''Advanced'' subsection within each of the chapter,
  that beginner could skip without missing the story??


* At the bottom of every page (excluding Getting Started) put link to other
chapters (maybe only ''prev'' and ''next'') --> code that!


* How to incorporate documentation on plot.ly/api/docs/:

+ Line and Scatter (s1)
+ Error Bars
+ Bubble Charts
+ Area plots
+ Box Plots
+ Heatmaps
+ Bar Charts
+ Histograms
+ Text Charts
+ Mixed Types
+ Time series

+ Multiple axes, Insets and Subplots

+ Layout: Axes, Legends(s1 and ), 
  Global Font, Annotations, IFrames, Sizing, Labels

+ File Settings: Privacy, File Sharing, Overwrite (s1), Append, Extend, Setting
  Layout, File Naming, Setting Style, Formal Syntax.

* From Matt (April 02):

+ Part of training should have a quick and easy 'plug and play' for the Python
API and matplotlib wrapper that would let the user read a csv and make plots
with it. If I could get a plot in say 5-10 lines of codes and have an easy way
to put in a csv e.g. http://www.stat.ubc.ca/~jenny/notOcto/STAT545A/examples/

+ Then, I could just read a few lines into the NB. Then, I could have a
different example where I could just put in my own csv and get a bar chart,
scatter, line, etc., for each of the plots. Something like that would be really
cool to have as easy examples, so that people who have data and literally just
want to put in the csv, run the code, and get a graph either with our example
or their data would be awesome, and be a cool way to get people up and running.
It's one thing that's sweet about the ggplot2 gallery where I can throw in 5 or
so lines of code and get a graph.

+ So, basically Matt would love a 'Template' section (possible in the appendix)





