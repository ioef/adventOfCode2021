#!/usr/bin/env python3
from collections import OrderedDict

with open("input", "r") as fileIn:
   depths = [line.strip() for line in fileIn.readlines()]

lst_len = len(depths)
idx = 1
sum = 0
while idx < lst_len:
    if int(depths[idx]) > int(depths[idx-1]):
        sum +=1
    idx +=1

print(sum)
