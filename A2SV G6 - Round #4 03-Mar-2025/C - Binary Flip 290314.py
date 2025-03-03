# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

t = int(input())

def solve ():
    size = int(input())
    binarya = input()
    binaryb = input()
    count = 0
    binarya += '0'
    binaryb += '0'
    
    for i in range(size):
        if binarya[i] == '1':
            count += 1
        else:
            count -= 1
            
        if ((binarya[i] == binaryb[i]) != (binarya[i + 1] == binaryb[i + 1])) and count != 0:
            print("NO")
            return
    print("YES")
        
for _ in range(t):
    solve()