# -*- coding:utf-8 -*-
#!/bin/bash

import string

'''
1.7 将字符串逐字符或逐词反转
'''

str = "python is the best of world !"
print str

revchars = str[::-1]
print revchars

revwords = str.split()
revwords.reverse()
revwords = ' '.join(revwords)
print revwords

revwords1 = ' '.join(str.split()[::-1])
print revwords1

import re
revwords2 = re.split(r'(\s+)', str)
revwords2.reverse()
revwords2 = ''.join(revwords2)
print revwords2

revwords3 = ''.join(re.split(r'(\s+)',str)[::-1])
print revwords3

revwords4 = ' '.join(reversed(str.split()))
print revwords4

revwords5 = ''.join(reversed(re.split('(\s+)',str)))
print revwords5


