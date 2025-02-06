# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums  = Counter(nums)

        ret = [0,0]
        print(nums)
        for i in nums:
            if nums[i] % 2 == 0:
                ret[0] += nums[i] // 2
            elif nums[i] > 2 and nums[i] % 2  :
                ret[0] += nums[i] // 2
                ret[1] += nums[i] % 2
            else:
                ret[1] += 1
        return ret 
        