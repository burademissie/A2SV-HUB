# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

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
            

        