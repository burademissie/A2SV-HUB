# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        last = float('-inf')
        for i in range(len(nums)-1 , -1 , -1):
            if last > nums[i]:
                return True

            while stack and stack[-1] < nums[i]:
                last = stack.pop()

            stack.append(nums[i])
        return False