# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        rot = [0] * n

        for i in range(n):
            rot[(i + k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = rot[i]