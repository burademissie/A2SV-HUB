# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            mini = i
            for j in range(i,len(nums)):
                if nums[mini] > nums[j]:
                    mini = j
            nums[mini] , nums[i] = nums[i] , nums[mini]
        
        answer = []

        for i in range(len(nums)):
            if nums[i] == target:
                answer.append(i)
        return answer

        