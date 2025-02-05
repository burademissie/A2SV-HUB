# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        listDict = {}
        common = defaultdict(int)

        for ind , string in enumerate(list1):
            listDict[string] = ind
        
        for i in range(len(list2)):
            if list2[i] in listDict:
                common[list2[i]] = i + listDict[list2[i]]
        
        ret  = [string for string in common.keys() if common[string]==min(common.values())]
        return ret
        
        
        