# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        multiples = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                multiples[nums[i] * nums[j]] += 1
        
        answer = 0

        for k in multiples.values():
            if k >= 2:
                answer += (4 * k * (k-1))

        return answer
                
            
        