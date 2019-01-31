# -*- codingutf-8 -*-
"""
Created on Sat Nov 17 10:10:57 2018

@author: shmbh
"""
# COnvert string1 to string2

string1 = "sunday"
string2 = "saturday"
m = len(string1)
n = len(string2)

## Create table

T = [[0 for x in range(n+1)] for z in range(m+1)] #[[Columns] rows]
#print(T)
## The string we want to convert is  columns
#print(T)

for i in range(m+1):
    for j in range(n+1):
        if i == 0: # First string is empty
            T[i][j] = j
        elif j == 0: # Second string is empty
            T[i][j] = i
            
        elif (string1[i-1] == string2[j-1]):
            T[i][j] = T[i-1][j-1]
        else:
            T[i][j] = 1+ min(T[i-1][j],T[i-1][j-1],T[i][j-1])

print(T[m][n]) # Print last element