#! /bin/bash
#
# Shortcut to clean up `config.json`, add, commit and push entire folder
#
# ===============================================================================

# clean up `config.json` 
#echo -e ("{ \
#      \"plotly_streaming_tokens\": [\"\", \"\", \"\"], \
#      \"plotly_api_key\": \"a35m7g6el5\", \
#      \"plotly_username\": \"etpinard\" \
#}" )
#
#exit 0 

#
git add --all

#
git commit -m "$1"

#
git push origin master

# -------------------------------------------------------------------------------
