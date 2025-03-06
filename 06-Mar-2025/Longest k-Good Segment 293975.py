# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
n , k = map(int,input().split())

nums = list(map(int,input().split()))

numset = defaultdict(int)
right = left = maxlen = 0
l = r = 0
while right < n:
    numset[nums[right]] += 1
    
    while len(numset) > k and left < n:
        numset[nums[left]] -= 1
        if numset[nums[left]] == 0:
            del numset[nums[left]]
        left += 1
    if right - left > maxlen:
        l = left
        r = right
        
        maxlen = right - left
    right += 1
print(l+1 , r+1)
        