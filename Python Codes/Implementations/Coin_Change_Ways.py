# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:52:46 2018

@author: shmbh
"""

coins = [2,5,3,6]
total = 10
no_coins = len(coins)

t =[[0 for i in range(total+1)] for j in range(no_coins)]  ##[[rows]columns]

for i in range(no_coins):  
    t[i][0] = 1

for i in range(no_coins):
    for j in range(total+1):
        if (j >= coins[i]):
            t[i][j] = t[i-1][j] + t[i][j-coins[i]]
        else:
            t[i][j] = t[i-1][j]
print(t[no_coins-1][total])


