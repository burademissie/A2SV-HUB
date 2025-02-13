# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        sett = set()
        maxlen = 0
        length = 0
        for i in range(len(s)):
            while s[i] in sett:
                sett.remove(s[j])
                j+=1
            
            sett.add(s[i])
            
            maxlen = max(maxlen , i - j + 1)
        return maxlen


        