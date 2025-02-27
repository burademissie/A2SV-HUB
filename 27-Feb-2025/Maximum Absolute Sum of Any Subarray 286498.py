# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxsum = minsum = minsums = maxsums = 0
        
        for num in nums:
            maxsums = max(0 , maxsums + num)
            minsums = min(0 , minsums + num)

            maxsum = max(maxsum , maxsums)
            minsum = min(minsums , minsum)
        return max(abs(minsum) , maxsum)




        