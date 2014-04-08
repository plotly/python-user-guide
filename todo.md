
List of ideas for this project
------------------------------

* Change the font for the IPython notebook. Code OK,
  Look Some good-looking sans serif

### `Getting Started` should have:

+ a quick intro
+ the Plotly logo embedded (find the histogram one)

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
+ Every notebook (or section) is intended to be a ''lecture''
+ mention the https://github.com/jiffyclub/open-in-nbviewer Chrome extension
+ (Matt on April 07) Make a notebook of all notebooks.

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

      - Maybe add 'text' option to fig 3. ('text': "maybe an out-lier") 
        
      - Will have to include info the 'help' function once it is online

+ 2) Bar Charts and Error Bars: 
      Example of csv reader (with Climate data from Environment Canada),
      Simplest bar chart, error bar, 
      horizontal bar charts, 
      2-panels, fully custom (maker/line color, gap, font size) bar chart, 
      annotation

      - fig 4: simple bar chart (T_avg and T_std, vertical)
      - fig 5: Horizontal bar+ error_x (value) (T_min, T_avg, T_max for JJA)
      - fig 6: Montreal vs. Vancouver T_avg and P_avg 
            (2-panels, tilt axis label, marker/line colors)

     Ask Jack about `Bar bottom` and `error_x` 
     cleanup folders 

     Maybe add a ''stack'' bar chart with cumulative rainfall in MTL and Van
     (maybe make that one horizontal and have fig 5 be a simple vertical)

+ 3) Bubble charts and (and Pandas)
      (use Jack''s nbviewer!!)

      - fig 7: bubble chart with pandas retrieval
      - fig 8. bubble chart (maybe)

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

      type: [box],  boxpoints: [all], jitter, pointpos

      maybe a gaussian fit example

      - fig 9: compare final exam grade, midterm grade (overlay)
      - fig 10: Add guassian fit to prev 
                (a few style options: highlight mean, mode, median, manual bins)
      - fig 11: subplot assignments, midterm, final, course (maybe ...)
      - fig 12: box plot assignments, midterm, final, course


+ 5) Heatmaps, 2d Histograms & color scales (use your function for polar_vortex)

+ Multiples axes and Insets (Multiple Axes, Subplots, Insets)
    example a retrieving data from plot. with browser!

    - A couple example of multiple axes in Feb28 plotly email

+ matplotlib converter
+ Polar Charts (coming soon)
+ Streaming Data
+ Retrieve Data from Plotly
+ 3d Surface Plots (coming soon)
+ Maps (coming soon)

+ (maybe) an FAQ section
+ List of Plotly style options with links to examples (in different chapter)! 
    --> code that with ''grep''!!!
+  Troubleshooting and debugging

+ Should I call put ''Advanced'' subsection within each of the chapter,
  that beginner could skip without missing the story??


* At the bottom of every page (excluding Getting Started) put link to other
chapters (maybe only ''prev'' and ''next'') --> code that! YES YES


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

+ Matt (April 07) Package chapters into folders makes sense. 

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




