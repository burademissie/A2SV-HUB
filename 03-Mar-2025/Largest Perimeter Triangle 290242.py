# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        right = len(nums) -1
        nums.sort()
        answer = 0
        while right >= 2:
            if nums[right-2] + nums[right-1] > nums[right]:
                answer = sum(nums[right-2:right+1])
                break
            
            right -= 1
        return answer

