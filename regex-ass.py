#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Finds the maximum and minimum number in a list
# In this assignment you will read through and parse a
# file with text and numbers. You will extract all the
# numbers in the file and compute the sum of the numbers.

import re

#hand = open('regex-sample.txt')
hand = open('regex-actual-ass.txt')
numlist = list()
for aline in hand:
    aline = aline.rstrip()
    stuff = re.findall('([0-9]+)', aline)
    if len(stuff) >=1:
        numlist.extend(stuff)

print "*" * 15, "\n"
print numlist
print len(numlist)

print "*" * 15, "\n"
newlist = list()
for jen in numlist:
    jen = int(jen)
    newlist.append(jen)

print "Maximum: ", max(newlist), "Minimum: " , min(newlist), "SUM: ", sum(newlist)
