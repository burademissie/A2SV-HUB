# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

inp = list(map(int,input().split()))

nums= list(map ( int , input().split()))

j = 0
maxj = 0
summ = 0

for i in range(inp[0]):
    summ += nums[i]
    while summ > inp[1]:
        summ -= nums[j]
        j+=1
    
    maxj = max(maxj,i-j+1)
print(maxj)
    
    
        