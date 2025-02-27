# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

b , r = map(int,input().split())

bulding = list(map(int,input().split()))

pre = [0] * b
suff = [0] * b

for i in range(b):
    if i > 0:
        if bulding[i] < bulding[i-1]:
            pre[i] = bulding[i-1] - bulding[i]
        else:
            pre[i] = 0
    else:
        pre[i] = 0

for i in range(b-1,-1 , -1):
    if i < b-1:
        if bulding[i] < bulding[i+1]:
            suff[i] = bulding[i+1] - bulding[i]
    else:
        suff[i] = 0

for i in range(b):
    if i>0:
        pre[i] = pre[i-1] + pre[i]
for i in range(b-1,-1,-1):
    if i<b-1:
        suff[i] = suff[i+1] + suff[i]

for _ in range(r):
    l , ri = map(int,input().split())
    
    
    if l < ri:
        print(pre[ri-1]-pre[l-1])
    else:
        print(suff[ri-1] - suff[l-1])
    
    