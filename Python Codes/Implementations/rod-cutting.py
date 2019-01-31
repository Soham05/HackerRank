# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:45:23 2018

@author: shmbh
"""
price=[1,5,8,9 ,10,17,17,20]
values=[0 for i in range(len(price)+1)]

n=len(values)
for i in range(1,n):
    maximum=-10000
    for j in range(0,i):
        maximum =max (maximum, price[j]+values[i-j-1])
    values[i]=maximum
print (values[n-1])