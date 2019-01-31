# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:04:24 2018

@author: shmbh
"""

val = [3, 34, 4, 12, 5, 2] 
sum = 9
n = len(val)

t = [[False for v in range(sum+1)]for s in range(n+1)]
print(t)

for i in range(n+1):
    t[i][0] = True

for i in range(sum+1):
    t[0][i] = False
     
for i in range(1,n+1):
    for j in range(1,sum+1):
        if (j < val[i]):
            t[i][j] = t[i-1][j]
        else:
            t[i][j] = t[i-1][j] or t[i-1][j-val[i]]

print(t[n][sum])
        