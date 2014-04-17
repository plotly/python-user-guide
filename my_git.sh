#! /bin/bash
#
# Shortcut to clean up `config.json`, add, commit and push entire folder
#
# Arguments:
# 
# 1) git commit message
# 2) git branch name
#
# ===============================================================================

# Define temporary file
tmp="/tmp/my_git"

# Clean up `config.json` 
cp config.json $tmp
cat config-stream-sample.json > config.json

# Add all files in sub-folders to git
git add --all

# Add commit message
git commit -m "$1"

# Push to master branch
git push origin "$2"

# Move filled-in config.json back to directory
mv $tmp config.json
# -------------------------------------------------------------------------------
