# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        answer = 0
        for char in s:
            if char == "L":
                balance += 1
            else:
                balance -= 1
            if not balance:
                answer += 1
        return answer
        