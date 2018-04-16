# -*- coding:utf-8 -*-
#!/bin/bash

import string

'''
1.9 简化字符串的translate方法的使用
'''

import string 
def translator(frm='', to='', delete='', keep=None):
    if len(to) == 1:
        to = to * len(frm)
    trans = string.maketrans(frm, to)
    if keep is not None:
        allchars = string.maketrans('', '')
        delete = allchars.translate(allchars, keep.translate(allchars, delete))
    def translate(s):
        return s.translate(trans, delete)
    return translate

digits_only = translator(keep=string.digits)
print digits_only('python world : 2018-04-10')

no_digits = translator(delete=string.digits)
print no_digits('python world : 2018-04-10')

digits_to_hash = translator(frm=string.digits, to='#')
print digits_to_hash('python world : 2018-04-10')

trans = translator(delete='python', keep='hello')
print trans('python world : 2018-04-10')
