# -*- coding:utf-8 -*-
#!/bin/bash

import string

'''
1.3  测试一个对象是否是类字符串
'''

def isAString(anobj):
    return isinstance(anobj, basestring)

print "isAString('python') :\t", isAString("python")
print "isAString(1234567890) :\t", isAString(1234567890)


