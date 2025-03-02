# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = map(int, input().split())

intervals = []
maxb = 0
mina = float('inf')

for _ in range(n):
    a, b = map(int, input().split())
    intervals.append((a, b))
    maxb = max(maxb, b)
    mina = min(mina, a)

nums = [0] * (maxb - mina + 2)

for a, b in intervals:
    nums[a - mina] += 1
    nums[b - mina + 1] -= 1


for i in range(1, len(nums)):
    nums[i] += nums[i - 1]

valid = [0] * len(nums)
for i in range(len(nums)):
    if nums[i] >= k:
        valid[i] = 1  
for i in range(1, len(valid)):
    valid[i] += valid[i - 1]


for _ in range(q):
    s, e = map(int, input().split())

   
    s = max(s, mina)
    e = min(e, maxb)

    if s > e:
        print(0)
    else:
        if s == mina:
            print(valid[e - mina])
        else:
            print(valid[e - mina] - valid[s - mina - 1])
