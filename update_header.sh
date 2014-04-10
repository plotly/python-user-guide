#! /bin/bash
#
# Script that updates the header cell in (all) IPython notebooks for this
# project.
#
# - The header cell is defined as the first `markdown` cell in the notebook's
#   .ipynb file, the first cell being the title. 
# 
# - The section 0 notebook is exempted from all updates.
#
# - This script takes one arguments, the name of notebook whose header is to
#   serve as 'model' for all other headers.
#
# ===============================================================================

## 0) A few definitions

# file of the model header is the first argument
model_file="$1"

# model starting line is
model_start="\"cell_type\": \"markdown\","

# model end line is 
model_end=" },"

# define a temporary file
tmp="/tmp/update_header"
tmp_header="/tmp/update_header-header"
tmp_above="/tmp/update_header-above"
tmp_below="/tmp/update_header-below"

# paths to notebooks (all but 's0_*' the first element)
all_paths=($(ls */*.ipynb))
paths=(${all_paths[@]:1})

# -------------------------------------------------------------------------------

## 1) Get model header 

# get line number of start of header
l_start=$(grep -Fn "$model_start" $model_file | head -n 1 | cut -d ":" -f 1)

# include '{' line above $model_start
l_start=$(($l_start-1))

# trim text above line $l_start into tmp file
tail -n +$l_start $model_file > $tmp

# get line number of end of header
l_end=$(grep -Fn "$model_end" $tmp | head -n 1 | cut -d ":" -f 1)

# trim $model_file down to just the header
head -n $l_end $tmp > $tmp_header

# -------------------------------------------------------------------------------

## 2) Substitute model header for all notebook in $paths

for i in ${paths[@]}; do

  # get line number of start of header in file $i
  l_start=$(grep -Fn "$model_start" $i | head -n 1 | cut -d ":" -f 1)

  # include '{' line above $model_start in file $i
  l_start=$(($l_start-1))
  
  # get trim text above line $l_start into tmp file
  head -n +$l_start $i | head -n -1 > $tmp_above

  # trim text above line $l_start into tmp file
  tail -n +$l_start $i > $tmp

  # get line number of end of header
  l_end=$(grep -Fn "$model_end" $tmp | head -n 1 | cut -d ":" -f 1)
  
  # remove '{' line above $model_start in file $i
  l_end=$(($l_end+1))
  
  # trim $model_file down to just the header
  tail -n +$l_end $tmp > $tmp_below

  ## concatenate back into $i
  echo -e "Updating ... $i"
  cat $tmp_above $tmp_header $tmp_below > $i

done

echo "done"
# -------------------------------------------------------------------------------
