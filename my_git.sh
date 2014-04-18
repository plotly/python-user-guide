#! /bin/bash
#
# Shortcut to add, commit and push entire folder
#
# Arguments:
# 
# 1) git commit message
# 2) git branch name
#
# ===============================================================================

# Add all files in sub-folders to git
git add --all

# Add commit message
git commit -m "$1"

# Push to master branch
git push origin "$2"

# -------------------------------------------------------------------------------
