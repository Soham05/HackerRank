# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 16:16:38 2018

@author: shmbh
"""

arr=[8,15,3,7]
n=len(arr)
table = [[0 for i in range(n)] for j in range(n)]
for gap in range(n): 
        for j in range(gap, n): 
            i = j - gap 
              
            # Here x is value of F(i+2, j),  
            # y is F(i+1, j-1) and z is  
            # F(i, j-2) in above recursive  
            # formula  
            x = 0
            if((i + 2) <= j): 
                x = table[i + 2][j] 
            y = 0
            if((i + 1) <= (j - 1)): 
                y = table[i + 1][j - 1] 
            z = 0
            if(i <= (j - 2)): 
                z = table[i][j - 2] 
            table[i][j] = max(arr[i] + min(x, y), 
                              arr[j] + min(y, z)) 
print (table[0][n - 1]) 