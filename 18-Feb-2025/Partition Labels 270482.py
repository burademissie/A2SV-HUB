# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars = defaultdict(int)
        for i , v in enumerate(s):
            chars[v] = i
        size = 0
        maxlen = 0
        answer = []
        for i in range(len(s)):
            size += 1
            maxlen = max(chars[s[i]] , maxlen)
            
            if i == maxlen:
                
                answer.append(size)
                size = 0
        return answer


        