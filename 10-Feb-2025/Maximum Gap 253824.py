# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        diff = []
        if n < 2:
            return 0
        for i in range(n-1):
            diff.append(nums[i+1] - nums[i])
        
        return max(diff)




        