# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        n = len(nums)
        prefix = [0] * n
        numsdict = defaultdict(int)
        numsdict[0] = 1
        answer = 0

        for i in range(n):
            prefix[i] = prefix[i-1] + nums[i]
        for j in range(n):
            if prefix[j] % k in numsdict:
                answer += numsdict[prefix[j] % k]
            numsdict[prefix[j] % k] += 1
        return answer

        