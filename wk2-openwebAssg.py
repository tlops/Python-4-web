#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# programming for web by Dr chuck
# University of Michigan
# Written as an assignment by Tlops
# Nov. 2015

# what this Code does:
# You are to retrieve the following document using the
# HTTP protocol in a way that you can examine the HTTP
# Response headers

# sample link:
# http://www.pythonlearn.com/code/intro-short.txt

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))

mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1):
        break
    print data

mysock.close()
