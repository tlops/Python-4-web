#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Finds the maximum, minimum  and sum of numbers in a list
# by extracting numbers in a string and creating a list.

import re


x= """ Why should you learn to write programs? 7746
12 1929 8827
Writing programs (or programming) is a very creative
7 and rewarding activity.  You can write programs for
many reasons, ranging from making your living to solving
8837 a difficult data analysis problem to having fun to helping 128
someone else solve a problem.  This book assumes that
everyone needs to know how to program ..."""



stuff = re.findall('([0-9]+)', x)
numlist = list()
for i in stuff:
    num = int(i)
    numlist.append(num)

total = sum(numlist)
print "TOTAL: ", total

print stuff
