# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        count = {0:-1}
        c = 0
        answer = diff = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c -= 1
            else:
                c += 1
            
            if c in count:
                answer = max(answer , i - count[c])
                
            else:
                count[c] = i
    
        return answer
        
        