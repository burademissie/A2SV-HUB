# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        answer = []
        third = len(nums)//3
        print(count)
        for key , value in count.items():
            if value > third:
                answer.append(key)
            print(key)
        return answer
            

        