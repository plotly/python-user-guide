from bs4 import BeautifulSoup

# -------------------------------------------------------------------------------
#
# Script that
#
# - redirects links to <h1> to #notebook
# - strips <h1> tag (i.e. the nb's title)
# - strips <style></style> inside body
# - strips <script></script> inside body (which inserts mathjax)
# - strips last <pre><pre> inside body (which inserts css into nb)
#
# -------------------------------------------------------------------------------

NAME = 'update_body'


# Replace href to title
def replace_title_href(body):
    old = "#"+body.h1['id']
    new = "#notebook"
    for a in body.findAll('a'):
        if a['href']==old:
            print "[{}]".format(NAME), '... link to title found:', a['href']
            a['href'] = a['href'].replace(old, new)
            print "[{}]".format(NAME), '... link updated to:', a['href']
    return body


# Strip title (i.e. the first h1) tag from body
def strip_title(body):
    body.h1.extract()
    print "[{}]".format(NAME), '... strip <h1> title'
    return body


# Strip style tag from body
def strip_style(body):
    body.style.extract()
    print "[{}]".format(NAME), '... strip <style>'
    return body


# Strip script tag from body
def strip_script(body):
    body.script.extract()
    print "[{}]".format(NAME), '... strip <script> (which inserts MathJax)'
    return body


# Strip last pre tag from body
def strip_last_pre(body):
    Pre = body.findAll('pre')
    Pre[-1].extract()
    for div in body.findAll('div')[::-1]:
        if all(i in div['class'] for i in ['cell','border-box-sizing','code_cell','rendered']):
            div.extract()
            break
    print "[{}]".format(NAME), '... strip last <pre> and parent <div> (which inserts CSS into NB)'
    return body

# -------------------------------------------------------------------------------


def update_body(body):
    body = replace_title_href(body)
    body = strip_title(body)
    body = strip_style(body)
    body = strip_script(body)
    body = strip_last_pre(body)
    return body
