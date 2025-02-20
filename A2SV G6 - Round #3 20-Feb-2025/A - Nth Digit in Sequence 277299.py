# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

num = int(input())
arr = []

for i in range(1,num+1):
    arr.append(str(i))
    
arr = "".join(arr)
print(arr[num-1])