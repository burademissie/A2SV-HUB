# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsCounter = Counter(nums)
        uniqueNum = set(nums)
        k = len(nums)//2
        for i in uniqueNum:
            if numsCounter[i]>k:
                return i



        