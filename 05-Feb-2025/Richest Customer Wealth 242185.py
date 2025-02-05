# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealths = set()

        for i in range(len(accounts)):
            wealths.add(sum(accounts[i]))
        
        return max(wealths)
            
        