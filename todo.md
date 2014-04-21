
List of ideas for this project
------------------------------

### The Tomorrow file

+ Get started on section 5! Heatmaps, 2d histograms and contours
 
  - leave maps for another sections

+ New Python API feautres: 

  See http://nbviewer.ipython.org/github/plotly/python-api/blob/1.0/notebooks/Plotly%20and%20Python.ipynb

  - Graph objects, classes for each type of dictionary
  - help() and .validate()
  - subplots generating function
  - get_figure and strip
  - credentials
  - get_subplots
  - Working in Python -> GUI -> back in Python
  - 

+ tell users to use pip to install pandas in section 3 and 5

+ Plotly names the 'traces' list as 'data'. Change that!

+ Change all URLs to nbviewer from /master/ to /1.0/ !!!

+ Should 1.4 be on new workflow and get_figure?? With Andrew's example

+ Rendering errors in nbviewer:
  
  - Resizing figure does not inside nbviewer
  - As well as the <center> </center> tags
  - cell width is also tricky (check CSS file)
  - the <code> tag too is not supported (even in v2.0)
  - can't set text-decoration: none for hyperlinks 

+ Why does In [] Out [] disappeared after running CSS file

+ Make all notebooks presentable!

  - s0 mostly done, except table of contents
  - s1 mostly done, except for 1.3
  - s2 mostly done
  - s3 one more bubble chart (log, multiple axes, line fit) 
  - s4 one more histogram (custom bins, area line)
  - s5 contour plots!

+ Have a 'line and scatter revisited' section with new API tools 

+ Mention Color brewer (at one point, )

+ add last code cell (the CSS one) to `update_footer`
 Or at least, make them consistent!

+ New Plotly defaults:

  - puts in a legend in even if len(traces)==1 
  - legend is placed outside axis frame
  - no axis frame
  - a much lighter grid


### `Getting Started` should have:

+ Table of Contents with links and full description 
    (including layout/style options covered, e.g. examples include )

+ Installation guidelines (info on api_key, add pictures!!!)

+ Sign up info --> Setup config.json as in streaming demos!

+ When will the new version -- with help() -- be released?

### Jack wants: 1 notebook for each of Plotly''s plot types

+ 1) Line & Scatter Plots:
      a simple first plot, 
      dictionaries/customization (plot type, color, style, title, 
      axis/legend labels), *** add ref to text chart plot type ** 
      file setting (file name, output, overwrite)
      plotly homepage (screenshot )
      formal syntax!

      - fig 1: Simplest line plot
      - fig 2: Line and marker plot
      - fig 3: Line and marker plot + a few layout options

      - Will have to include info the 'help' function once it is online

+ 2) Bar Charts and Error Bars: 
      Example of csv reader (with Climate data from Environment Canada),
      Simplest bar chart, error bar, 
      horizontal bar charts, 
      2-panels, fully custom (maker/line color, gap, font size) bar chart, 
      annotation

      - fig 4: simple bar chart (T_avg and T_std, vertical)
      - fig 5: Direct labels overlaid (T_min, T_avg, T_max for JJA)
      - fig 6: horizontal stacked (P mtl and van)
      - fig 7: Montreal vs. Vancouver T_avg and P_avg 
            (2-panels, tilt axis label, marker/line colors)

     Ask Jack about `Bar bottom` and `error_x` 

+ 3) Bubble charts and (and Pandas)
      (use Jack''s nbviewer!!)

      - fig 8: bubble chart with pandas retrieval 
               Set population in million!
      - fig 9. bubble chart (maybe)

      Maybe make this `Bubble charts and Multiple axes` 
      (GDP and LifeExp vs time, )

      Maybe add an `area plot` (i.e. filled)

+ 4) Histograms and box plots
      Want to show how to make the Plotly logo??
      Talk about 'barmode': 'stack' in here maybe? (use ATMS 211 Class marks?)

      type: [histogramx, histogramy, histogram2d] ,
      barmode: [stack, overlay, group] ,
      autobinx: [False], xbins: [start,end, size], 
      histnorm: [count, percent, probability, density, probability density]

      no need (I think) to go over marker: [color, line]  and bardir: ['h']

      type: [box],  boxpoints: [all,outliers,False], jitter, pointpos

      maybe a gaussian fit example

      - fig 10: compare final exam grade, midterm grade (overlay)
      - fig 11: compare histnorm values (2x2 panel plot)
      - fig 12: autobinx: False
                (a few style options: highlight mean, mode, median, manual bins)
                maybe Gaussian fit
      - fig 14: box plot assignments, midterm, final, course


+ 5) Heatmaps, 2d Histograms & color scales 
      use your function for polar_vortex to describe color bar
    
      - fig 15:
      - fig 16:
      - fig 17:

+ Multiples axes and Insets (Multiple Axes, Subplots, Insets)
    example a retrieving data from plot. with browser!

    - A couple example of multiple axes in Feb28 plotly email

+ matplotlib converter
+ Polar Charts (coming soon)
+ Streaming Data
+ Retrieve Data from Plotly
+ 3d Surface Plots (coming soon)
+ Maps (coming soon)  --> with a shapefile maybe

### Misc. Thoughts

+ What writing style to use? How about:
  - Use We/Let''s for demonstrations and thing
  - Use ''you'' for things not included in the document (e.g. try it!)

+ Convention: 

  - write doc string for functions to be used in multiples cells, not otherwise 
  - use same function/variable name if only used in one cell

+ Use LaTeX symbols at one point on a plot

+ Make an FAQ section or appendix

+ List of Plotly style options with links to examples (in different chapter)! 
    - code that with ''grep''!!!
    - like a reference table

+  Troubleshooting and debugging appendix

+ Should I call put ''Advanced'' subsection within each of the chapter,
  that beginner could skip without missing the story??

* At the bottom of every page (excluding Getting Started):

  - put link to  ''prev'', ''next'' and front page  (could be better looking)
  - Add the Plotly logo, contact info! (not bad)

+ remove plotly.__version__ line in Section 2 and up

+ remember that not every one is using Unix-like systems.

+ make a folder on Plotly folder for documentation figs ??

+ header comments should all start with Upper case, 
  inline comment with lower case

+ Find a clever way to label figure and sections?


### How to incorporate documentation on plot.ly/api/docs/:

+ Line and Scatter (s1)
+ Error Bars (s2)
+ Bubble Charts
+ Area plots
+ Box Plots 
+ Heatmaps
+ Bar Charts (s2)
+ Histograms
+ Text Charts (where ???)
+ Mixed Types (good example online, without in s5 with heatmaps)
+ Time series (in the streaming section)

+ Multiple axes, Insets and Subplots

+ Layout: Axes, Legends(s1 and ), 
  Global Font (s2), Annotations (s2), IFrames, Sizing (s2), Labels (s1)

+ File Settings: Privacy, File Sharing, Overwrite (s1), Append, Extend, Setting
  Layout, File Naming, Setting Style, Formal Syntax.

### From Matt (April 02):

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

### Form Python User Feedback (April 07):

+ But that''s part of the beauty of Plotly, that the default styling already
  beats the pants off Matplotlib, right?

+ As before, people love that they can make pretty graphs. 

+ A few pieced of feedback that were oft mentioned:
  - People want to show private graphs in an IPython NB (most popular ask, I think).
  - Exporting graphs with an IPython NB when you export the NB.
  - Getting grid and column access from the API. (in new version)
  - Examples to replicate with my own data. (!!! templates ...)

+ Others that came up:
  - Handling more data, loading faster.
  - Instagraph for styling something in the GUI or with Python and then re-using
    that styling (in new version)
  - Being able to delete files (maybe add files to a folder and then delete it).
  - Sharing a plot directly as part of a API call.
  - Full description of the API and options available. (in new version)
  - Pre-defined colormaps. (in new version)
  - Have `.plotly_settings` file in the home directory and put key/username
    there so users don''t need to share username and key to share code.
    (in new version)

### Misc info

+ Available fonts in Plotly: 
  -  Arial, sans-serif,
  -  Courier New, monospace
  -  Droid Sans, sans-serif
  -  Droid Serif, serif
  -  Droid Sans Mono, sans-serif
  -  Georgia, serif
  -  Gravitas One, cursive
  -  Impact, Charcoal, sans-serif
  -  Lucida Console, Monaco, monospace
  -  Old Standard TT, serif
  -  Open Sans, sans-serif
  -  PT Sans Narrow, sans-serif
  -  Raleway, sans-serif
  -  Times New Roman, Times, serif
  -  Verdana, sans-serif




