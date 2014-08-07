# Make instructions

## Contents:

+ The typical workflow

+ Available make targets

+ Philosophy

-------------------------------------------------------------------------------

### The typical workflow

1. List all notebooks to be included in the plot.ly user guide in 
   `./makefile` under the variable `ug-nbs`.

2. Fill in `./scripts/inputs/translate.json` where the keys are the paths 
   (relative to `./`) to the notebooks to be converted and the 
   values correspond to the user-guide URL tails on plot.ly. 

3. Run `$ make convert` to convert these notebooks to HTML

4. Run `$ make publish` to adapt these HTML notebooks for plot.ly!  This make
   call outputs 1 HTML template `body.html` and 1 `config.json` file for each
   notebook making the user guide.

5. Run `$ make-push-to-streambed` to copy the relevant file structure to 
   the `streambed/` repo (assumed to be one level down in your path).

Once step 1 to 5 are completed and that `streambed/` is updated, run
`$ make link-nbs-to-plotly` and update the remote repo to link the notebooks 
on nbviewer to plot.ly (hence redirecting traffic to plot.ly!). 

-------------------------------------------------------------------------------

### Available make targets:

+ `instructions` :
    - cat this file

+ `convert` :
   - convert notebooks to HTML using `ipython nbconvert`
   - move those notebooks to `./converted/`

+ `publish` :
    - [scripts/translate_href-html.py] translate inter-NB hyper refs pointing to
      nbviewer, the local directory or plotly external (i.e.
      https://plot.ly/...) to django internal (/python/..) using
      `scripts/inputs/{translate.json,domains.json}`.
    - [scripts/publish.py] strip the HTML body from style tags, remove undesired
      cells, print results in `./published/<url-tail>/body.html` where
      <url-tail> is taken from `scripts/inputs/translate.json`.
    - [scripts/make_config.py] generate a config.json for each notebook with
      meta info and etc. 
      
+ `push-to-streambed`:
    - copy published subdirectories to `streambed` (assuming `streambed/` in 
      one level down in your path).

+ `link-nbs-to-plotly`:
    - [scripts/translate_href-ipynb] translate inter-NB hyper-refs pointing to
      nbviewer or the local directory to plotly external (i.e.
      https://plot.ly/..) in the (original .ipynb) notebooks.

+ `clean-converted`:
    - clear `./converted/`

+ `clean-published`:
    - clear `./published/*`

+ `clean`:
    - `clean-converted` then `clean-published`

-------------------------------------------------------------------------------

### Philosophy

+ The notebooks on nbviewer path MUST be keep intact so that reader do not end
  up on dead or out-dated links. DO not change the NBs' filename and stay on the
  master branch.

+ All scripts used for the makefile are in `./scripts/`.

+ All (hard-coded) inputs data files are `./scripts/inputs/` , with the
  exception of the `ug-nbs` variable in `./makefile`.

+ `./converted/` stores HTML notebooks (an intermediate step ignored by git).

+ `./published/` stores `streambed/`-ready content.

-------------------------------------------------------------------------------
