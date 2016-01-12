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
# This code looks for span tags and pull out the text
# content of the span tag, convert them to integers and add them up

# test link:
# http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.html  = 2553
# http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_191501.html   = 2402

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
total = 0   # initialize total
for tag in tags:
   #print 'URL:',tag.get('class', None)
   total += int(tag.contents[0])

print total
