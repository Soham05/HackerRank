# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:52:51 2018

@author: shmbh
"""
coins = [1,2,5]
total = 5
no_coins = len(coins)

t =[[float("inf") for i in range(total+1)] for j in range(no_coins)]  ##[[rows]columns]

for i in range(no_coins):
    t[i][0] = 0

for i in range(1,no_coins):
    for j in range(total+1):
        if (j < coins[i]):
            t[i][j] = t[i-1][j]
        else:
            t[i][j] = min(t[i-1][j],1+t[i][j-coins[i]])
print(t[no_coins-1][total])
