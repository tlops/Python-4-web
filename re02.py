#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Finds the maximum and minimum number in a list
import re

hand = open('mbox-short.txt')
numlist = list()
for aline in hand:
    aline = aline.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', aline)
    if len(stuff) !=1: continue
    num = float(stuff[0]) # converting string to float
    numlist.append(num)
print "Maximum: ", max(numlist), "Minimum: " , min(numlist)
        #a = re.findall('^From (\S+@\S+)', aline)#.group(0)
        #print a

print "####################"

x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
x1 = "We just received $10.00 for cokies and $15 for oranges or $7.05 for mango"
y1 = re.findall('\$[0-9.]+', x1)    # extract the money(s)
y = re.search('\S+@\S+',x).group(0) # extract email
z = re.findall('^From .*@([^ ]*)',x) # extract domain name
x2 = 'From: Using the : character'
y3 = re.findall('^F.+:', x2)

print "Y3", y3
print "Z", z
print "Y", y
print  "Y1",y1
#print "Z1", z1
