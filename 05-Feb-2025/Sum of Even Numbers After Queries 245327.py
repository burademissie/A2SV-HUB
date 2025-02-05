# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        summ = sum(num for num in nums if num % 2 == 0)

        ret = []

        for query in queries:
            if nums[query[1]] % 2 == 0:
                summ -= nums[query[1]]

            nums[query[1]] += query[0]

            if nums[query[1]] % 2 == 0:
                summ += nums[query[1]]
            
            ret.append(summ)
        return ret
                    
        