# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        answer = 0
        ret = 0
        for word in words:
            answer = 0
            for i in range(len(word)):
                if word[i] in allowed:
                    answer += 1
            if answer == len(word):
                ret += 1
        return ret

        