# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n , k = map(int,input().split())

nums = list(map(int,input().split()))

diff = []

for i in range(1,n):
    diff.append(nums[i] - nums[i-1])

diff.sort()
ans = 0

if n == k:
    print(0)
elif k==1:
    print(sum(diff))
else:
    ans += sum(diff[:-k+1])
    print(ans)