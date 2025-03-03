# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

n , m = map(int,input().split())
prefix = []
for i in range(n):
    c , t = map(int,input().split())
    prefix.append(c*t)
    if i > 0:
        prefix[i] += prefix[i-1]

moment = list(map(int,input().split()))

j = 0
for i in range(len(moment)):

    while prefix[j] < moment[i]:
        j += 1
    print(j+1) 