#! /bin/bash
#
# Shortcut to clean up `config.json`, add, commit and push entire folder
#
# ===============================================================================

# clean up `config.json` 
# ...

#
git add --all

#
git commit -m "$1"

#
git push origin master

# -------------------------------------------------------------------------------
