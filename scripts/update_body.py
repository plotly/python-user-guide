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

# -------------------------------------------------------------------------------


# Wrap tag around an other
# source: http://stackoverflow.com/a/10192634
def wrap(wrappend, wrap_tag, wrap_attrs):
    _soup = BeautifulSoup()
    wrapper = _soup.new_tag(wrap_tag, **wrap_attrs)
    contents = wrappend.replaceWith(wrapper)
    wrapper.append(contents)
    return


# Strip contents inside tag but keep tag
def strip_contents(tag):
    for content in tag.contents:
        if content == u'\n':  # Need this to not mess up loop
            pass
        else:
            content.extract()
    return


# Insert tag inside an other
# source: http://stackoverflow.com/a/21356230/4068492
def inserter(insertend, insert_tag, insert_attrs,
             insert_content, replace=True):
    _soup = BeautifulSoup()
    to_insert = _soup.new_tag(insert_tag, **insert_attrs)
    to_insert.string = insert_content
    if replace:
        strip_contents(insertend)
    insertend.append(to_insert)
    return

# -------------------------------------------------------------------------------


# Replace href to title
def replace_title_href(body):
    old = "#"+body.h1['id']
    new = "#notebook"
    for a in body.findAll('a'):
        if a['href'] == old:
            print "[{}]".format(NAME), '... link to title found:', a['href']
            a['href'] = a['href'].replace(old, new)
            print "[{}]".format(NAME), '... link updated to:', a['href']
    return body

# -------------------------------------------------------------------------------


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
        if all(i in div['class']
               for i in ['cell', 'border-box-sizing',
                         'code_cell', 'rendered']):
            div.extract()
            break
    print (
        "[{}]".format(NAME),
        '... strip last <pre> and parent '
        '<div> (which inserts CSS into NB)'
    )
    return body


# Strip.
def strip(body):
    body = strip_title(body)
    body = strip_style(body)
    body = strip_script(body)
    body = strip_last_pre(body)
    return body

# -------------------------------------------------------------------------------


# Add anchor to In/Out <div> (for easy link sharing)
def add_anchors(body):
    insert_tag = 'a'
    a_class = "anchor-link"
    for div in body.findAll('div', {"class": "prompt"}):
        text = div.getText(strip=True, separator=u' ')
        if not text:
            continue
        # Add id attr to <div>
        _id = text.replace(" ", "-").replace(u"\xa0", "-").lower()
        div['id'] = _id
        # Add <a href= > around text
        a_href = '#' + _id
        insert_attrs = {'href': a_href, 'class': a_class}
        inserter(div, insert_tag, insert_attrs, text)
    return body

# -------------------------------------------------------------------------------


def update_body(body):
    body = replace_title_href(body)
    body = strip(body)
    body = add_anchors(body)
    return body
