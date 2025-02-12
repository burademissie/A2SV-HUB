# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        res=[]
        while j>i and skill[i+1]:
            if skill[i]+skill[j] == skill[i+1]+skill[j-1]:
                res.append(skill[i]*skill[j])
                j-=1
                i+=1
            else : return -1
        return sum(res)
        