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

The User Guide assume the latest version (v 1.0) of Plotly's Python API verison
1.0. The latest version features many improvements. For instance: 

* *get* function, to import data and plot options from public figures, 
* A *help* function, 
* Easier manipulation and customization of lists and dictionaries through 
  *graph objects*,
* Subplot generating function,
* Credentials setup.


#### Content

The User Guide is entirely written inside [IPython
notebooks](http://ipython.org/notebook.html). 

This Github repository is divided into folders, where each folder contains 
one IPython notebook and their required data files.

The User Guide homepage is folder `s00_homepage` and the notebook can be found
[here](http://nbviewer.ipython.org/github/etpinard/plotly-python-doc/tree/1.0/s00_homepage/s00_homepage.ipynb).

Current sections:

* [Section 0:](http://nbviewer.ipython.org/github/etpinard/plotly-python-doc/tree/1.0/s0_getting-started/s0_getting-started.ipynb)
  Getting Started with Plotly (`s0_getting-started`)

* [Section 1:](http://nbviewer.ipython.org/github/etpinard/plotly-python-doc/tree/1.0/s1_line-scatter/s1_line-scatter.ipynb)
  Line & Scatter Plots (`s1_line-scatter`)

* [Section 2:](http://nbviewer.ipython.org/github/etpinard/plotly-python-doc/tree/1.0/s2_bar-charts/s2_bar-charts.ipynb)
  Bar Charts & Error Bars (`s2_bar-charts`)

* [Section 3:](http://nbviewer.ipython.org/github/etpinard/plotly-python-doc/tree/1.0/s3_bubble-charts/s3_bubble-charts.ipynb)
  Bubble Charts (`s3_bubble-charts`)

* [Section 4:](http://nbviewer.ipython.org/github/etpinard/plotly-python-doc/tree/1.0/s4_histograms/s4_histograms.ipynb)
  Histograms & box plots (`s4_histograms`)

* [Section 5:](http://nbviewer.ipython.org/github/etpinard/plotly-python-doc/tree/1.0/s4_histograms/s5_heatmaps.ipynb)
  Heatmaps, Contours & 2D Histograms (`s5_heatmaps`)


#### Other files in this repo


* `plotly-python-doc.css`: CSS file for notebook styling

* `my_git.sh`: git add, commit and push shortcut

* `update_footer.sh`: update footer of all notebooks

* `update_header.sh`: update header of all notebooks

* `make_folder.sh`: Makes subfolder `Readme.md` files,
   print header and footer in notebook (to do!)

* `todo.md`: list of ideas for this project (not official by any means)

* `api-v1-test.ipnb`: notebook filled with v1.0 tests

#### Installation guidelines

Step 1. The User Guide assume :
  
* Plotly version 1.0 **Important**
* Python version 2.7.5+
  - with `numpy`, `scipy`, `pandas` installed
* IPython version 2.0.0

Step 2. To install Plotly, use pip:
  - `$ pip install plotly` or
  - `$ sudo pip install plotly`

Step 3. Check version (inside Python or IPython), upgrade if needed:

`>>> import plotly`

`>>> print plotly.__version__`

* If not up latest (`1.0.0`) version:
  - `$ pip install plotly --upgrade`

Step 4. Sign up for Plotly if you don't have an account already:

* Go to [plot.ly](https://plot.ly) and click on the *Sign up* button.

Step 5. Get username and API key:

* After signing in, click the Settings tab,
* Your API key and username are under Profile.

Step 6. For better code portability, we recommend setting up a credentials file:

* In Python or IPython

  `>>> import plotly.tools as tls`
 
  `>>> tls.set_credentials_file(username="<-->", api_key="<-->")`

Where the username and api_key keys are filled in with your own.

This creates a .credentials file in your $HOME/.plotly/ folder storing the
username and API key locally in JSON file.

* You can access your credentials in Python/IPython with:

  `>>> my_creds = tls.get_credentials_file()`

Step 7. Sign in to Plotly from Python API:

`>>> import plotly.plotly as py`    

`>>> import plotly.tools as tls`   

`>>> my_creds = tls.get_credentials_file()`

`>>> py.sign_in(my_creds['username'], my_creds['api_key'])`

And there you go. You are now ready to make plots using Plotly and the Python
API.  Using the credentials file allows users to share code without having to
type in (yet along remember) their own username and API key every time they
want to generate a new Plotly plot.

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

* [Lorena A. Barba](http://lorenabarba.com/blog/announcing-aeropython/#.U1ULXdX1LJ4.google_plusone_share)

![Plotly logo](http://i.imgur.com/i6YeveO.png)

