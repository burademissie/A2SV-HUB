# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        prefix = [0] * (len(nums))

        for i in range(len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        count = 0
        
        for pre in prefix:
            if (pre - k) in seen:
                count += seen[pre-k]
            seen[pre] += 1
        return count
            
            

        


        