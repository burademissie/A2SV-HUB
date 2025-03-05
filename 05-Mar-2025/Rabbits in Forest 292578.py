# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        answer = 0

        for g , f in count.items():
            size = g + 1
            nog = math.ceil(f / size)
            answer += nog * size
        return answer 

        