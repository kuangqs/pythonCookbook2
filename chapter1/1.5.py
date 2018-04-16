# -*- coding:utf-8 -*-
#!/bin/bash

import string

'''
1.5 去除字符串两端的空格
'''

str = "python".center(100, " ")
print "str :\t", str, "end" 
print "str.lstrip() :\t", str.lstrip(), "end" 
print "str.rstrip() :\t", str.rstrip(), "end" 
print "str.strip() :\t", str.strip(), "end" 
print "str.strip(' pn') :\t", str.strip(' pn')
