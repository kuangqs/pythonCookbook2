# -*- coding:utf-8 -*-
#!/bin/bash

import string

'''
1.8 检查字符串中是否包含某字符集合中的字符
'''

seq = "python world"
aset = "abcdefghijklmnopqrstuvwxyz "

def containsAny(seq, aset):
    for c in seq:
        if c in aset: return True
    return False
print containsAny(seq,aset)

import itertools
def containsAny1(seq, aset):
    for item in itertools.ifilter(aset.__contains__, seq):
        return True
    return False
print containsAny1(seq,aset)

def containsAny2(seq, aset):
    return bool(set(aset).intersection(seq))
print containsAny2(seq,aset)

def containsOnly(seq, aset):
    for c in seq:
        if c not in aset: return False
    return True
print containsOnly(seq, aset)

def containsAll(seq, aset):
    return not set(aset).difference(seq)
print containsAll(seq, "p")



