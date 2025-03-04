# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        i = 0
        diff = []
        for a , b in costs:
            diff.append(((a - b) , i))
            i += 1
        
        diff.sort(reverse = True)
        ans = 0
        print(diff)
        change = 0
        for v , i in diff:
            a , b = costs[i]
            
            if change < len(costs)//2:
                
                ans += b
                change += 1
            else:
                ans += a
                change += 1
        return ans





        