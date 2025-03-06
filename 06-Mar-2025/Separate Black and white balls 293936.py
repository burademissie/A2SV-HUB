# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        right = left = len(s) - 1
        tot = 0
        while left >= 0:
            
            if s[left] == '1':
                tot += right - left
                right -= 1
            left -= 1
        return tot

        
        