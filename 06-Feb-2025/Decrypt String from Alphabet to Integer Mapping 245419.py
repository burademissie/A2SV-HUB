# Problem: Decrypt String from Alphabet to Integer Mapping - https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        atoi = defaultdict(int)
        jtoz = defaultdict(str)

        for i in range(97,106):
            atoi[i - 96] = chr(i)
        for i in range(106,123):
            jtoz[i - 96] = chr(i)
        print(atoi)
        i = len(s) - 1
        answer = ""       
        while i >= 0:
            if s[i]=="#":
                answer += jtoz[int(s[i-2:i])]
                i-=3
            else:
                answer += atoi[int(s[i])]
                i-=1
        return answer[::-1]
        