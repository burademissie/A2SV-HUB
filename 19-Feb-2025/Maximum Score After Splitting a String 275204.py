# Problem: Maximum Score After Splitting a String - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        left_zeros = 0
        right_ones = s.count('1')
        max_score = 0

        for i in range(len(s)-1):
            if s[i]=='0':
                left_zeros+=1
                # 1
            else:
                right_ones-=1
                # 3
            max_score= max (max_score,(left_zeros+right_ones))
            print(max_score)
            #                0      , 1+4 = 5 
            #5
            #5                5   ,   1+3 = 4

        return max_score
        