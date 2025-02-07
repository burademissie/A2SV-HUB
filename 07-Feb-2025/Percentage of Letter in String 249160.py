# Problem: Percentage of Letter in String - https://leetcode.com/problems/percentage-of-letter-in-string/description/%20meaning/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = Counter(s)
        summ = sum(list(count.values()))
        print(summ)
        print(count[letter])
        return floor((count[letter]/summ) * 100)        