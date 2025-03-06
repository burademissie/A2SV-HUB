# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict

t = int(input())

life = defaultdict(int)

for _ in range(t):
    b , d = map(int,input().split())
    
    life[b] += 1
    life[d] -= 1

keys = sorted(list(life.keys()))
pre = []
for i in range(len(keys)):
    pre.append([keys[i],life[keys[i]]])

for i in range(len(keys)):
    if i > 0:
        pre[i][1] += pre[i-1][1] 
maxn = float('-inf')
for y , n in pre:
    
    if n > maxn:
        newy = y
        maxn = n
print(newy , maxn)