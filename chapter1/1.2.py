# -*- coding:utf-8 -*-
#!/bin/bash

import string

'''
1.2 字符和字符值之间的转换
'''

print "ord('a') :\t", ord('a')

print "chr(97) :\t", chr(97)

print "ord(u'\u2020') :\t", ord(u'\u2020') 

print "repr(unichr(8224)) :\t", repr(unichr(8224))

print "repr(chr(97)) :\t", repr(chr(97))

print "repr(str(97)) :\t", repr(str(97))

print "map(ord, 'python') :\t", map(ord, 'python')

print "''.join(map(chr, range(97,100))) :\t", ''.join(map(chr, range(97,123)))


