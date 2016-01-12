#!/usr/bin/env python
# -*- coding: utf-8 -*-
# programming for web by Dr chuck
# University of Michigan
# Written as an assignment by Tlops

import urllib
from BeautifulSoup import *
# you need to install pip and BeautifulSoup to run this code
# you can find help here:
# http://stackoverflow.com/questions/12228102/how-to-install-beautiful-soup-4-with-python-2-7-on-windows

url = raw_input("Enter: ")

html = urllib.urlopen(url).read() # read the link
soup = BeautifulSoup(html) #
# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes
numurl = 0
numurlhttps = 0
tags = soup('a') # <a href=http://www.blabla> like a dictionary
for tag in tags:
    print tag.get('href', None) # removes the href
    numurl +=1      # increase link count
    #if ("youtube" in str(tag.get('href'))):
    if ("youtube" in str(tag.get('href'))): # check for secure links
        numurlhttps +=1         # increase secure link counts


print "There are ",numurl, " links on the submitted link"
print "There are ", numurlhttps, " https links on this page", url
