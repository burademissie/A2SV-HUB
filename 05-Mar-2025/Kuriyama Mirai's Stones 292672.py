# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

t = int(input())

stone = list(map(int,input().split()))
stonepre = [0] * t
stonepre[0] = stone[0]
for i in range(1,t):
    stonepre[i] =stonepre[i-1] + stone[i]
stone.sort()
sortstonepre = [0] * t
sortstonepre[0] = stone[0]
for i in range(1,t):
    sortstonepre[i] =sortstonepre[i-1] + stone[i]


q = int(input())
for _ in range(q):
    typ , l , r = map(int,input().split())
    l -= 1
    r -= 1
    
    if typ == 1:
        if l == 0:
            print(stonepre[r])
        else:
            print(stonepre[r] - stonepre[l-1])
    else:
        if l==0:
            print(sortstonepre[r])
        else:
            print(sortstonepre[r] - sortstonepre[l-1])
    