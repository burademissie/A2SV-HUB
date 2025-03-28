# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tot = 0
        start = 0
        for i in range(len(gas)):
            tot += gas[i] - cost[i]
            if tot < 0:
                tot = 0
                start = i + 1
        return start
            
            
        

        