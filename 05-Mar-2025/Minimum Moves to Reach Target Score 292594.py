# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target-1
        move = 0
        
        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                target //= 2
                maxDoubles -= 1
                
            elif maxDoubles == 0:
                move += (target - 1)
                break
            else:
                target -= 1
            move += 1
        return move