#-*-coding:utf-8-*-
__author__ = 'bj'
import string
import os
import re
content="ActivityRecord{43242 u0 com.tencent.mm/.plugin t2}"
pattern = re.compile(r'[a-z.]+/[a-z.]+')
match = pattern.findall(content)
if match:
    print match[0].replace("/","")
