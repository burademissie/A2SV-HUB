# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        difference = [0] * (n+1)
        for start, end , dir in shifts:
            
            if dir == 1 :
                difference[start] += 1
                difference [end+1] -= 1
            else:
                difference[start] -= 1
                difference[end+1] += 1

        for i in range(1,n+1):
            difference[i] += difference[i-1]
        
        res = []

        for i in range(n):
            shift = difference[i] % 26
            new_val = ord(s[i]) + shift
            if new_val > 122:
                new_val -= 26
            if new_val < 97:
                new_val += 26
            res.append(chr(new_val))
        return "".join(res)


