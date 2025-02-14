# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        minsum = float('inf')
        for i in range(len(nums)-1):
            left , right = i + 1 , n - 1 

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if abs(target - minsum) > abs(target - currentSum):
                    minsum = currentSum
                
                if currentSum > target :
                    right -= 1
                
                elif currentSum < target:
                    left += 1
                
                else :
                    return currentSum
                
        return minsum

            






        