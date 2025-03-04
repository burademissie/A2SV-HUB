# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tens = fives = 0
        
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                fives -= 1
            else:
                if not tens and fives>2:
                    fives -= 3
                else:
                    fives -= 1
                    tens -= 1
            
            if tens < 0 or fives < 0:
                return False
    
        return True

        