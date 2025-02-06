# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicate = Counter(nums)
        return [i for i in duplicate if duplicate[i]==2 ]
        # return list(duplicate.keys())  

        
        