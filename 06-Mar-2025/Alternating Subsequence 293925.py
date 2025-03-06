# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())

for _ in range(t):
    n = int(input())
    
    nums = list(map(int,input().split()))
    
    
    tot = 0
    right = 0
    while right < n:
        maxpos = 0
        minneg = float('-inf')
        while right < n and nums[right] > 0:
            maxpos = max(maxpos,nums[right])
            right += 1
        while right < n and nums[right] < 0:
            minneg = max(minneg,nums[right])
            right += 1
        if minneg != float('-inf'):
            tot += maxpos + minneg
        else:
            tot += maxpos
    print(tot)