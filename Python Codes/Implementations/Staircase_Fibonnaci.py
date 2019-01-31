# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:07:05 2018

@author: shmbh
"""

s=5 # Stair to reach
m=2 # number of ways we can climb

arr = [0 for i in range(s+1)]
arr[0],arr[1] = 1,1
print(arr)
for i in range(2,s+1):
    j = 1
    while j<=m and j<=i:
        arr[i] = arr[i] + arr[i-j]
        j = j+1
        print(arr)

print(arr[s])
