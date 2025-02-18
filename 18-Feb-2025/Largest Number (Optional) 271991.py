# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))

        def compare(x , y):
            if x + y > y + x:
                return -1
            else:
                return 1
        
        
        nums.sort(key=cmp_to_key(compare))
        if nums[0] == '0':
            return "0"

        nums = "".join(nums)
        return nums

        
        

            

            



        