# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left , right)
        
        def merge( left:List[int] , right:List[int] ):
            answer = []
            i = 0
            j = 0
            while i < len(left) and j<len(right):
                if left[i] < right[j]:
                    answer.append(left[i])
                    i+=1
                else:
                    answer.append(right[j])
                    j+=1
                
            answer.extend(left[i:])
            answer.extend(right[j:])
            return answer

        return merge_sort(nums)





            
        