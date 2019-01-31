# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:07:48 2018

@author: shmbh
"""

string1 = 'AGGTAB'
string2 = 'GXTXAYB'
n = len(string1)
m = len(string2)

t = [[0 for j in range(m+1)]for i in range(n+1)]
print(t)
    
for i in range(n+1):
    for j in range(m+1):
        if i == 0 or j == 0:
            t[i][j] = 0
        elif (string1[i-1] == string2[j-1]):
            t[i][j] = t[i-1][j-1] + 1
        else:
            t[i][j] = max(t[i-1][j],t[i][j-1])
print(t)
print(t[n][m])



