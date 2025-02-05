# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = 0
        count1 , count2 = Counter(s1) , Counter(s2)
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                diff+=1
        return (count1==count2) and (diff==2 or diff == 0)
        