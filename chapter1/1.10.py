# -*- coding:utf-8 -*-
#!/bin/bash

import string

'''
1.10 过滤字符串中不属于指定集合的字符
'''

allchars = string.maketrans('', '')
def makefilter(keep):
    delchars = allchars.translate(allchars, keep)
    def thefilter(s):
        return s.translate(allchars, delchars)
    return thefilter

if __name__ == '__main__':
    just_vowels = makefilter('aeiou')
    print just_vowels('hello every body, welcome to python world!')
    print just_vowels('good good study, day day up!')
