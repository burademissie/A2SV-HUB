# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

t = int(input())
if t%2 == 0:
    midian = t//2 -1
else:
    midian = t//2

nums = list(map(int,input().split()))
nums.sort()
print(nums[midian])