# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C

n , t , c = map(int,input().split())

pri = list(map(int,input().split()))

left = 0
ans = 0

for right in range(n):
    if pri[right] > t:
        left = right + 1
    
    currlen = right - left + 1
    if currlen >= c:
        ans += 1
print(ans)