# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        nums = [i for i in range(int(sqrt(c)+1))]
        print(nums)
        i , j = 0 , len(nums)

        
 
            

        while i <= j :
            if i * i + j * j < c:
                i += 1
            elif i * i + j * j > c:
                j -= 1
            
            elif i * i + j * j == c:
                return True
        return False

        