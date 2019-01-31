# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:56:22 2018

@author: shmbh
"""

arr = [2,-1,4,3,5,-1,3,2]
n = len(arr)
print(arr)
list1 = [1]*len(arr)
#print(list1)
list2 = [1]*len(arr)
#print(list2)

for i in range(1,n):
    for j in range(0,i):
        if arr[i] > arr[j] and list1[i] < list1[j]+1:
            list1[i] = list1[j]+1
print(list1)
for i in reversed(range(n-1)): #loop from n-2 downto 0 
        for j in reversed(range(i-1 ,n)): #loop from n-1 downto i-1 
            if(arr[i] > arr[j] and list2[i] < list2[j] + 1): 
                list2[i] = list2[j] + 1
print(list2)

maximum = list1[0] + list2[0] - 1
for i in range(1,n):
    maximum = max((list1[i] + list2[i] - 1),maximum)
print(maximum)