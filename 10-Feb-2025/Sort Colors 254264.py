# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = {0:0,1:0,2:0}
        for i in nums:
            count[i]+=1
            print(count)
        nums[:count[0]]=[0]*count[0]
        nums[count[0]:count[0]+count[1]]=[1]*count[1]
        nums[count[0]+count[1]:count[0]+count[1]+count[2]]=[2]*count[2]