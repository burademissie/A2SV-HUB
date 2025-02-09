# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n-1:
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
                i+=2
            else:
                i+=1
        ans = []
        for i in nums:
            if i != 0:
                ans.append(i)
        ans.extend([0]*(n-len(ans)))
        return ans
        