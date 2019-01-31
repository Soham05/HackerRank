# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:57:14 2018

@author: shmbh
"""
wt = [1,3,4,5]
values = [1,4,5,7]
totwt = 7

n = len(values) # Total number of items

## Building a matirx
K = [[0 for j in range(totwt+1)] for i in range(n)]
print(K)

for i in range(n):
  K[i][0]=0

for j in range(1,totwt+1):
  K[0][j]=values[0]

for i in range(1,n):
    for j in range(1,totwt+1):
        if (j < wt[i]):
            K[i][j] = K[i-1][j]
        else:
            K[i][j] = max(values[i]+K[i-1][j-wt[i]],K[i-1][j])
    print("after run::",K)
print(K[n-1][totwt])