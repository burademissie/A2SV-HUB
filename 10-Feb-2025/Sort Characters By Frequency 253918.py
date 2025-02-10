# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorte =sorted(count,key=lambda x:count[x],reverse=True)
        
        answer = ""
        for i in sorte:
            answer += i * count[i]
        return answer
        