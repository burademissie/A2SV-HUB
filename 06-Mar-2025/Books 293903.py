# Problem: Books - https://codeforces.com/contest/279/problem/B

n , t = map(int,input().split())

nums = list(map(int,input().split()))

cursum = 0
left = maxlen = 0
for right in range(n):
    cursum += nums[right]
    while cursum > t:
        cursum -= nums[left]
        left += 1
    maxlen = max(maxlen , right - left + 1)
print(maxlen)
    