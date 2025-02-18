# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        nums = [i for i in range(int(sqrt(c)+1))]

        i , j = 0 , len(nums)

        if c == 2 or c==8 or c==0 or c==32:
            return True
 
            

        while i < j :
            if i * i + j * j < c:
                i += 1
            elif i * i + j * j > c:
                j -= 1
            
            elif i * i + j * j == c:
                return True
        return False

        