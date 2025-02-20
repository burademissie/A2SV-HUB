# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

test= int(input())

for t in range(test):
    x , heights = map(int,input().split())
    heightarr = list(map(int,input().split()))
    
    heightarr.sort()
    
    
    
    front = 0
    back = x
    
    count = 0
    while front < x:
        if heightarr[front] + heights <= heightarr[front+back]:
            count += 1 
        front += 1
    if count == x:
        print("YES")
    else:
        print("NO")