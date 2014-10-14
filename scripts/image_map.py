from bs4 import BeautifulSoup
import json
import os
import sys
import urllib
import shutil

# -------------------------------------------------------------------------------
#
# Script that
#
# - lists all image links,
# - downloads them and
# - converts the sources to the appropriate relative path.
#
# N.B. There is only one image folder for all user guide notebooks per language
#
# -------------------------------------------------------------------------------

NAME = "image_map"  # file name
IMAGE_REPO = "published/static/image/"
IMAGE_SB = "/static/api_docs/image/user_guide/python/"


# Get HTML soup from HTML file path
def get_soup(file_html):
    with open(file_html, "r") as f:
        print "[{}]".format(NAME), 'Opening', file_html
        return BeautifulSoup(f)


# Find file functions
def find(file_path):
    file_dir, file_name = os.path.split(file_path)
    for root, dirs, files in os.walk(file_dir):
        if file_name in files:
            return os.path.join(root, file_name)
        else:
            return False


# Make directory tree
def make_tree(tree):
    if not os.path.exists(tree):
        print "[{}]".format(NAME), '... making', tree
        os.makedirs(tree)
    else:
        print "[{}]".format(NAME), '...', tree, 'already exists OK'

# -------------------------------------------------------------------------------


# Get image name in IMAGE_REPO and IMAGE_SB
def get_img_name(img_src, img_i):
    # get extension
    _, img_ext = os.path.splitext(img_src)
    # name images in order, starting from image01
    if img_i < 10:
        img_name = "image0{i}{ext}".format(i=img_i, ext=img_ext)
    else:
        img_name = "image{i}{ext}".format(i=img_i, ext=img_ext)
    return img_name


# Get required paths in this repo for this NB
def get_paths_repo(file_html, translate):
    file_html_base = os.path.basename(file_html)
    for old, leaf in translate.items():
        old_base = os.path.basename(old).replace('.ipynb', '.html')
        if old_base == file_html_base:
            dir_ipynb = os.path.dirname(old)
            return {'dir_ipynb': dir_ipynb}
    else:
        print "[{}]".format(NAME), '!!! URL tail not found in translate.json'


# Get images!
def image_get(files_html, translate):
    make_tree(IMAGE_REPO)
    img_map = dict()
    img_i = 0
    for file_html in files_html:
        soup = get_soup(file_html)
        for img in soup.findAll('img'):
            img_src = img['src']
            if (not img_src.startswith('data:image/png;base64')
                    and not img_src in img_map.keys()):
                # if not raw png, or not already in list, add to map
                img_i += 1
                img_name = get_img_name(img_src, img_i)
                # define new paths to image
                img_path_repo = os.path.join(IMAGE_REPO, img_name)
                img_path_sb = os.path.join(IMAGE_SB, img_name)
                if img['src'].startswith(('https://', 'http://')):
                    # (1) if sourced via https/http, add to list to download
                    print (
                        "[{}]".format(NAME), '... https/https image src!',
                        img_src)
                    print (
                        "[{}]".format(NAME), '... download as',
                        img_path_repo)
                    urllib.urlretrieve(img_src, img_path_repo)
                else:  # TODO test this case!
                    paths_repo = get_paths_repo(file_html)
                    img_src_abs = os.path.join(paths_repo['dir_ipynb'],
                                               img_src)
                    if find(img_src_abs):
                        # (2) if sourced via relative link, add to list to copy
                        print (
                            "[{}]".format(NAME), '... local image src!',
                            img_src)
                        print (
                            "[{}]".format(NAME), '... copy image to',
                            img_path_repo)
                        shutil.copy(img_src_abs, img_path_repo)
                    else:
                        print (
                            "[{}]".format(NAME), '!!! weird image src',
                            img_src)
                        print "[{}]".format(NAME), '... do nothing.'
                        continue
                # fill in image map dict (for image_replace_src)
                img_map[img['src']] = img_path_sb
    return img_map

# -------------------------------------------------------------------------------


# Replace image source!
def image_replace_src(soup, img_map):
    for img in soup.findAll('img'):
        for old, new in img_map.items():
            if img['src'] == old:
                print "[{}]".format(NAME), '... image source:', old
                print "[{}]".format(NAME), '... translated to:', new
                img['src'] = img['src'].replace(old, new)
    return soup
