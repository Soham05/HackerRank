# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 11:22:09 2018

@author: shmbh
"""

price = [1, 5, 8, 9, 10, 17, 17, 20]  # prices of each lenght i.e for lenght the price is 20.
n = len(price) # length of rod

T = [[0 for n in range(n)]for p in range(len(price))]

for i in range(n+1):
    for j in range(i,n+1):
        if j >= i:
            T[i][j] = max(T[i-1][j],price[i]+T[i][j-i])
        else:
            T[i][j] = T[i-1][j]

print(T[n][n])