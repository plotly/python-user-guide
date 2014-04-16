Plotly's Python API User Guide
===============================

Welcome to [Plotly's](https://plot.ly) Python API User Guide

The User Guide was written with the goal of giving Plotly Python (and IPython)
users extensive documentation on almost all of Plotly's features. 

Whereas Plotly's [web documentation and
gallery](https://plot.ly/api/python/docs) is meant to serve Plotly beginners
just looking to make a simple plot and experienced users trying out a new plot
type.  The User Guide intends to make beginner and intermediate Plotly users
experts.


#### Content

The User Guide is entirely written inside [IPython
notebooks](http://ipython.org/notebook.html). 

This Github repository is divided into folders, where each folder contains 
one IPython notebook and their required data files.

Current sections:

* [Section 0:](http://nbviewer.ipython.org/github/etpinard/plotly-python-doc/blob/master/s0_getting-started/s0_getting-started.ipynb)
  Getting Started with Plotly (`s0_getting-started` folder)

* [Section 1:](http://nbviewer.ipython.org/github/etpinard/plotly-python-doc/blob/master/s1_line-scatter/s1_line-scatter.ipynb)
  Line & Scatter Plots (`s1_line-scatter`)

* [Section 2:](http://nbviewer.ipython.org/github/etpinard/plotly-python-doc/blob/master/s2_bar-charts/s2_bar-charts.ipynb)
  Bar Charts & Error Bars (`s2_bar-charts`)

* [Section 3:](http://nbviewer.ipython.org/github/etpinard/plotly-python-doc/blob/master/s3_bubble-charts/s3_bubble-charts.ipynb)
  Bubble Charts (`s3_bubble-charts`)

* [Section 4:](http://nbviewer.ipython.org/github/etpinard/plotly-python-doc/blob/master/s4_histograms/s4_histograms.ipynb)
  Histograms & box plots (`s4_histograms`)

Proposed future sections:

* Section 5: Heatmaps, 2D histograms
* Section 6: Contour plots and Maps
* Section ?: Polor charts, 3D plots, Streaming Data, Retrieve data from Plotly
* and others
* Appendix A: Complete list of Plotly style options
* Appendix B: FAQ
* Appendix C: Useful templates (for users looking to 'plug and play')


#### Config file and other files in this repo

* `config.json`: JSON file containing username, api key and stream tokens

* `config-sample.json`, `config-stream-sample.json: Sample `config.json` files

* `my_git.sh`: Re-init. config.json, git add, commit and push 

* `update_footer.sh`: update footer of all notebooks

* `update_header.sh`: update header of all notebooks

* `make_folder.sh`: Makes subfolder `Readme.md` files,
   print header and footer in notebook (to do!)

* `todo.md`: list of ideas for this project (not official by any means)

* `plotly-python-doc.css`: CSS file for notebook styling


#### Versions, Installation and Configuration

* At the moment, this project assumes :
  - plotly version 0.5.13
  - python version 2.7.5+
  - ipython version 2.0.0

* To install Plotly (for Unix-like users): 
  - Either use pip: `$ pip install plotly`
  - Or try: `$ sudo pip install plotly`

* Check version (inside python or ipython): 
  - `>>> import plotly`
  - `>>> print plotly.__version__`

* If not up latest version:
  - `$ pip install plotly --upgrade`

* Get username and APi key by signing in at [plot.ly](https://plot.ly/)
  - For better code portability, we recommend filling in a JSON file 
    named `config.json` (see `config-sample.json` for syntax)


#### Want to improve the User Guide

While reading the User Guide, if ever:

* you have a suggestion for a new chapter, 
  you would like to include more information about a particular plot option,
  you caught some spelling and grammar mistakes 

  ... Tell us about it. Or, change it yourself.

* Fork us! All commits are welcomed!

#### Got Questions and Feedback? 

* About Plotly
  email at feedback@plot.ly 
  or tweet at [@plotlygraphs](https://twitter.com/plotlygraphs)

* About the User Guide
  email at etienne.t.pinard@gmail.com
  or tweet at [@etpinard](https://twitter.com/etpinard)

#### Big Thanks to

* [Cam Davidson-Pilon](http://nbviewer.ipython.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Prologue/Prologue.ipynb) 
  for notebook styling ideas


![Plotly logo](http://i.imgur.com/i6YeveO.png)

