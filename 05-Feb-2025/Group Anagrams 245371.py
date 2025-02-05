# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = defaultdict(list)

        for string in strs:
            key = str(sorted(list(string)))
            wordDict[key].append(string)

        return list(wordDict.values())

        