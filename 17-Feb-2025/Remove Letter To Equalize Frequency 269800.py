# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)
        frequency = [fre for fre in count.values()]
        for i in range(len(frequency)):
            frequency[i] -= 1
            if len(set(frequency)) == 1:
                return True
            if frequency[i] == 0:
                if len(set(frequency)) == 2:
                    return True
            frequency[i] += 1
        return False
        