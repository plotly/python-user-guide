#! /bin/bash

# from repo parent path
parent=$PWD
tmp="tmp.ipynb"

for nb_path in s*/*.ipynb; do

    dir=$(dirname $nb_path)
    cd $dir

    nb=$(basename $nb_path)
    cmd="ipython $parent/scripts/nb_execute.py $nb $tmp"
    eval $cmd
    mv -f $tmp $nb

    cd $parent

done
