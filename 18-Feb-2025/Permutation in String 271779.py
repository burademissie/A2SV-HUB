# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = Counter(s1)
        counts2 = Counter(s2[:len(s1)])
        
        if counts2 == counts1:
            return True
        for i in range(len(s1),len(s2)):
            
            counts2[s2[i-len(s1)]] -= 1
            if counts2[s2[i-len(s1)]] == 0:
                del counts2[s2[i-len(s1)]]
            counts2[s2[i]] += 1
            if counts2[s2[i]] <= 0:
                del counts2[s2[i]]
            if counts2 == counts1:
                return True
            
        return False        