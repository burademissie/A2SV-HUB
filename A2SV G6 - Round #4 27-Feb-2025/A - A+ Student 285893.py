# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

from collections import Counter

t = int(input())


def solve(arr):
    sett = Counter(arr)
    maxs = max(arr)
    ans = []
    if len(sett) == 1:
        return [1]*3
    elif arr[0] != arr[1] and arr[1] != arr[2] and arr[0]!= arr[2]:
        for num in arr:
            if maxs == num:
                ans.append(0)
            else:
                ans.append(maxs - num + 1)
    elif len(sett) == 2:
        if sett[maxs] == 2:
            for num in arr:
                if num != maxs:
                    ans.append(maxs - num +1)
                else:
                    ans.append(1)
        else:
            for num in arr:
                if num != maxs:
                    ans.append(maxs -num + 1)
                else:
                    ans.append(0)
    return ans
        


for _ in range(t):
    nums = list(map(int, input().split()))

    print(*solve(nums))
        
    