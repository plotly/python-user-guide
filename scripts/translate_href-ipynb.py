import json
import sys

# -------------------------------------------------------------------------------
# 
# Script that converts inter-User Guide href in ipynb (i.e. original) NBs
# to plot.ly domain (using ./inputs/translate.json)
#
# ??? Should I also translate the relative links ???
#
# -------------------------------------------------------------------------------

NAME="translate_href-ipynb"  # file name

# Get input arguments 
def get_args():
    args = sys.argv[1:]
    if not args:
        print ("usage:\n"
               "python {NAME}.py file.html \n"
               "python {NAME}.py file1.html file2.html ...  fileN.html\n".format(NAME=NAME))
        sys.exit(0)
    else:
        return args

# Get URLs of domains 
def get_domains():
    return dict(
        nbviewer="http://nbviewer.ipython.org/github/plotly/python-user-guide/blob/master/",
        plotly="https://plot.ly/python/"  # the web page
    )

# Get translate.json, to translate URL tails from 
# nbviewer to plot.ly domain
# (e.g. s00_homepage/s00_homepage.ipynb to home
def get_translate():
    with open('./scripts/inputs/translate.json') as f:
        translate = json.load(f)
    return translate

# -------------------------------------------------------------------------------

# Get the NB json object
def get_NB(file_ipynb):
    with open(file_ipynb, "r") as f:
        print "[{}]".format(NAME), 'Opening', file_ipynb
        return json.load(f)
        
# Replace 'nbviewer'-domain hrefs to plot.ly
def replace_href(NB, domains, translate):
    for i_cell, cell in enumerate(NB['worksheets'][0]['cells']):
        if cell['cell_type']=='markdown':
            for i_line, line in enumerate(cell['source']):
                if domains['nbviewer'] in line:
                    _line=line.replace(domains['nbviewer'],domains['plotly'])
                    print "[{}]".format(NAME), '... link found in cell {} / line {}'.format(i_cell,i_line)
                    for old, new in translate.items():
                        if old in _line:
                            __line=_line.replace(old,new)
                            NB['worksheets'][0]['cells'][i_cell]['source'][i_line]=__line
                            print "[{}]".format(NAME), '... line updated to:', __line
                            #TODO! Print raw string instead
                            break
    return NB
                
# Replace ipynb file 
def replace_file_ipynb(NB_new, file_ipynb):
    with open(file_ipynb, "wb") as f:
        print "[{}]".format(NAME), '... overwrites', file_ipynb
        json.dump(NB_new, f, indent=4)
        return

# -------------------------------------------------------------------------------

def main():

    files_ipynb = get_args()
    domains = get_domains()
    translate = get_translate()

    for file_ipynb in files_ipynb:
        NB = get_NB(file_ipynb)
        NB_new = replace_href(NB, domains, translate)
        replace_file_ipynb(NB_new, file_ipynb)

if __name__ == "__main__":
    main()
