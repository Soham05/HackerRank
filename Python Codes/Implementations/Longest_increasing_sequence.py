# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 13:20:55 2018

@author: shmbh
"""
import sys
import math

arr = [10, 22, 9, 33, 21, 50, 41, 60] 
print(arr)
n = len(arr)
list1 = [1]*n
#finallis = []
print(list1) 

for i in range(1,n):
    for j in range(0,i):
        if arr[i] > arr[j] and list1[i] < list1[j]+1:
            list1[i]=list1[j]+1
print(list1)
