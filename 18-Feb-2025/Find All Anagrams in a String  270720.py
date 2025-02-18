# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        countP = Counter(p)
        countS = Counter(s[:len(p)])
        answer = []
        if countS == countP:
            answer.append(0)

        for i in range(len(p),len(s)):
            
            countS[s[i-len(p)]] -= 1
            if countS[s[i-len(p)]] == 0:
                del countS[s[i-len(p)]]
            countS[s[i]] += 1
            
            if countS == countP:
                answer.append(i-len(p)+1)
            
        return answer
