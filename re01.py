#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

#fhandler = open('mbox-short.txt')
#for line in fhandler:
#    line = line.rstrip()
#    if line.find('From') >= 0:
#        print line

hand = open('mbox-short.txt')
for aline in hand:
    aline = aline.rstrip()
    if re.search('^From:', aline):
        print aline
print "####################"

x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.search('\S+@\S+',x).group(0) #
print y
