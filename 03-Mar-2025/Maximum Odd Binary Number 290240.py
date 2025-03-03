# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = Counter(s)
        answer = ""
        if count['1'] >= 2:
            answer += '1' * (count['1'] -1) 
            answer += '0' * count['0']
            answer += '1'
        else:
            answer += '0' * count['0']
            answer += '1'
        return answer

        