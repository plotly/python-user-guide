#! /bin/bash
#
# Shortcut to add, commit and push entire folder
#
# Arguments:
# 
# 1) git branch name
# 2) git commit message
#
# ===============================================================================

# Add all files in sub-folders to git
git add --all

# Add commit message
git commit -m "$2"

# Push to master branch
git push origin "$1"

# -------------------------------------------------------------------------------
