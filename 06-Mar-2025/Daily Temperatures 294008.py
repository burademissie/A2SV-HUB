# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i , temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                curtemp , ind = stack.pop()
                ans[ind] = i-ind
            stack.append([temp,i])
        return ans

            
        