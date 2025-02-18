# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minimum = float("inf")
        answer = float("-inf")
        total = 0
        for num in nums:
            total += num
            answer = max(answer, total)
            answer = max(answer, total - minimum)
            minimum = min(minimum, total)

        return answer