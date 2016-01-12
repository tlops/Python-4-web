#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# programming for web by Dr chuck
# University of Michigan
# Written as an assignment by Tlops
# Nov. 2015

# what this code does:
# The program will prompt for a URL, read the JSON data from that URL
# using urllib and then parse and extract the comment counts from the
# JSON data, compute the sum of the numbers in the file

# sample link:
# http://python-data.dr-chuck.net/comments_42.json (sum = 2482)
# http://python-data.dr-chuck.net/comments_191502.json


import json
import urllib

while True:
    url = raw_input('Enter URL: ')
    if len(url) < 1 : break

    print '\nRetrieving: ', url
    urlhandler = urllib.urlopen(url) # open url
    output = urlhandler.read()       # read url

    infojs = json.loads(output)     # json is parsed here
    #print infojs
    result = infojs["comments"]
    #print result
    print 'Comment count: ', len(result)

    total = 0       # initialiaze total
    for js in result:
        total =total + int(js['count'])
    print total
