#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# programming for web by Dr chuck
# University of Michigan
# Written as an assignment by Tlops
# Nov. 2015

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

# what this code does:
# The program uses urllib to read the HTML from the data files below
# extract the href= vaues from the anchor tags, scan for a tag that is in
# a particular position relative to the first name in the list, follow that
# link and repeat the process a number of times and report the last name
# you find.

# sample link: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this
# process 4 times.The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = input('Enter Count: ')
position = input('Enter Position: ')
position = position - 1 # human readable position

def open_url(url):
    # This funtion takes in url and returns tags
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
    tags = soup('a')
    return tags

def search_url(tags):
    # This function takes in tags usually the open_url method
    # and return a new url at a particular position in the list
    # of tags.
    for pos,tag in enumerate(tags):
        if pos == position: # checks for the position
            new_url = tag.get('href', None)
            print new_url
            return new_url

tags = open_url(url)
new_url= search_url(tags)
count = count - 1
while count > 0:
    new_tag = open_url(new_url)
    new_url = search_url(new_tag)
    count = count - 1
