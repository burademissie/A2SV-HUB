# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderdic = {0:-1}
        remainder = 0
        for i in range(len(nums)):
            remainder += nums[i]
            remainder %=k
            if remainder not in remainderdic:
                remainderdic[remainder] = i
            elif i - remainderdic[remainder] >=2:
                return True
        return False
        