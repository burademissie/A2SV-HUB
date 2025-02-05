# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numsCounter = Counter(nums)
        uniqueNum = set(nums)
        k = len(nums)//3
        ret = []
        for i in uniqueNum:
            if numsCounter[i]>k:
                ret.append(i)
        return ret
        
        