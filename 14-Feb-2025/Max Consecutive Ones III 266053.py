# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        r=l=0
        length = 0
        maxlength = length
        for r in range(len(nums)):
            if nums[r]==0 :
                k-=1
            if k<0:
                if nums[l]==0:
                    k+=1
                l+=1
        return r-l+1
        