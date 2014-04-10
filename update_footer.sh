#! /bin/bash
#
# Script that updates the footer cell in (all) IPython notebooks for this
# project.
#
# - The footer cell is defined as the last `markdown` cell in the notebook's
#   .ipynb file, the first cell being the title. 
# 
# - This script takes one arguments, the name of notebook whose footer is to
#   serve as 'model' for all other footers.
#
# - Try to incorporate cell above footer 
#   (tricker as link depend on the notebook)
#
# ===============================================================================

## 0) A few definitions

# file of the model footer is the first argument
model_file="$1"

# model starting line is
model_start="\"cell_type\": \"markdown\","

# model end line is 
model_end=" },"

# define a temporary file
tmp="/tmp/update_footer"
tmp_footer="/tmp/update_footer-footer"
tmp_above="/tmp/update_footer-above"
tmp_below="/tmp/update_footer-below"

# paths to notebooks (all of them, unlike update_header.sh)
all_paths=($(ls */*.ipynb))

# -------------------------------------------------------------------------------

## 1) Get model footer 

# get line number of start of footer
l_start=$(grep -Fn "$model_start" $model_file | tail -n 1 | cut -d ":" -f 1)

# include '{' line above $model_start
l_start=$(($l_start-1))

# trim text above line $l_start into tmp file
tail -n +$l_start $model_file > $tmp

# get line number of end of footer
l_end=$(grep -Fn "$model_end" $tmp | head -n 1 | cut -d ":" -f 1)

# trim $model_file down to just the footer
head -n $l_end $tmp > $tmp_footer

# -------------------------------------------------------------------------------

## 2) Substitute model footer for all notebook in $paths

for i in ${all_paths[0]}; do

  # get line number of start of footer in file $i
  l_start=$(grep -Fn "$model_start" $i | tail -n 1 | cut -d ":" -f 1)

  # include '{' line above $model_start in file $i
  l_start=$(($l_start-1))
  
  # get trim text above line $l_start into tmp file
  head -n +$l_start $i | head -n -1 > $tmp_above

  # trim text above line $l_start into tmp file
  tail -n +$l_start $i > $tmp

  # get line number of end of footer
  l_end=$(grep -Fn "$model_end" $tmp | head -n 1 | cut -d ":" -f 1)
  
  # remove '{' line above $model_start in file $i
  l_end=$(($l_end+1))

  # trim $model_file down to just the footer
  tail -n +$l_end $tmp > $tmp_below

  ## concatenate back into $i
  cat $tmp_above $tmp_footer $tmp_below > $i

done

# -------------------------------------------------------------------------------
