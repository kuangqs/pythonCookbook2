# -*- coding:utf-8 -*-
#!/bin/bash

import string

'''
1.1 每次处理一个字符
'''

thestring = "wertyuiopasdfghjklzxcvbnm,1234567890-"

thelist = list(thestring)
print thelist

for c in thestring:
    print c,
print "\n"

results_toUpper = [ c.upper() for c in thestring ]
print results_toUpper

results_map = map(string.upper, thestring)
print results_map



