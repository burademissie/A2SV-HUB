# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        right , left ,boat= len(people)-1 , 0 , 0
        people.sort()
        while left <= right:
            if people[right] + people[left] <= limit:
                left += 1
            
            right -= 1
            boat += 1

        return boat
        
        

        