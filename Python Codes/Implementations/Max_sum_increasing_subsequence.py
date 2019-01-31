# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:14:40 2018

@author: shmbh
"""

arr = [1, 101, 2, 3, 100, 4, 5] 
#max_arr = arr  Cannot use this because we never make copies of two lists it's just referencing
max_arr = arr.copy()

print(max_arr)

for i in range(1,len(arr)):
    for j in range(i):
        if (arr[i] > arr[j] and max_arr[i] < max_arr[j]+arr[i]):
            max_arr[i] = max_arr[j]+arr[i]
print(max(max_arr))
