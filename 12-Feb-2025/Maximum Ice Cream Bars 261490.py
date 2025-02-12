# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxc = max(costs) +1
        lis = [0] * maxc

        for i in costs:
            lis[i] += 1
        count = 0
        print(lis)
        for j in range(maxc):
            if lis[j] > 0:
                if j > coins:
                    break 

                maxbuy = min(lis[j] , coins//j)
                coins -= maxbuy * j
                count += maxbuy
        return count

            



        