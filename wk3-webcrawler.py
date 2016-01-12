#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# programming for web by Dr chuck
# University of Michigan
# Written as an assignment by Tlops
# Nov. 2015

import urllib
fhand = urllib.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print line.strip()
