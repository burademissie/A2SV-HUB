# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = list(s)
        for i in range(len(s)):
            shuffled[indices[i]] = s[i]

        return "".join(shuffled)
       

        