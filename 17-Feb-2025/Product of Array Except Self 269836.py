# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1 : return [0] * len(nums)

        product = math.prod(nums)
        prod_wout_0 = 1

        for n in nums:
            if n==0: continue    
            else:
                prod_wout_0 *= n
        res = []
        for n in nums:
            if n==0:
                res.append(prod_wout_0)
            else:
                res.append(product//n)

        return res    