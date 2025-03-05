# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    ansr = 0
    ansb = 0
    currsum =0
    for i in range(n):
        currsum += r[i]
        ansr = max(ansr ,currsum)
    currsum = 0
    for i in range(m):
        currsum += b[i]
        ansb = max(ansb , currsum)
    
    print(ansr + ansb)