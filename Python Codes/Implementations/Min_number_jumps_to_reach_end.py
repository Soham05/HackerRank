# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:51:08 2018

@author: shmbh
"""

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)

t = [0 for i in range(n)]

if n == 0 or arr[0]==0:
    print("Can't jump")

for i in range(1,n):
    t[i] = float('inf') ##nSO that min is not always 0 which we initiated to above!
    for j in range(i):
        if (i <= j + arr[j]) and (arr[j]!=float('inf')) :
            t[i] = min(t[i],t[j]+1)
            break
print(t[n-1])
            
            
    
    
    