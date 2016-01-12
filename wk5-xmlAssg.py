#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# programming for web by Dr chuck
# University of Michigan
# Written as an assignment by Tlops
# Nov. 2015

# what this code does:
# This program will prompt for a URL, read the XML data from that URL
# using urllib and then parse and extract the comment counts from
# the XML data, compute the sum of the numbers in the file.

# sample links (sum):
# http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.xml  (2553)
# http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_191498.xml  (2439)

import urllib
import xml.etree.ElementTree as ET

while True:
    url = raw_input('Enter URL: ')
    if len(url) < 1 : break

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    #print data
    tree = ET.fromstring(data)
    results = tree.findall('comments/comment') # creates a lists of comments
    print "Number of comments: ", len(results)
    #print results
    total=0
    for i in results:
        # go through the list and find the count tags
        lat = int(i.find('count').text) # extract the text in count tag
        total = total + lat     # add the values

    print "The Total is: ", total
    print " "
