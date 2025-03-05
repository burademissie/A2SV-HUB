# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())

for _ in range(t):
    n = int(input())
    
    arr = list(map(int,input().split()))
    diff = [0] * n
    for i in range(n):
        if i>0:
            diff[i] = arr[i-1] - arr[i]
    i = 0
    ans = 0
    while i < n:
        if diff[i] > 0:
            i += 1
            ans += 1
        i += 1
    print(ans)