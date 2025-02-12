# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

from collections import defaultdict


inp = int(input())



for i in range(inp):
    matrix = []
    rowcol = list(map(int , input().split()))
    for j in range(rowcol[0]):
        lis = list(map(int,input().split()))
        matrix.append(lis)
    
    diagonal = defaultdict(int)
    non = defaultdict(int)
    
    
    for k in range(rowcol[0]):
        for l in range(rowcol[1]):
            diagonal[k-l] += matrix[k][l]
            non[k+l] += matrix[k][l]
            
    
    max_sum = 0 
    for m in range(rowcol[0]):
        for n in range(rowcol[1]):
            
            # print(max_sum)
            summ = diagonal[m-n] + non[m+n] - matrix[m][n]
            
            max_sum = max(summ,max_sum)
    print(max_sum)
            
    
    
