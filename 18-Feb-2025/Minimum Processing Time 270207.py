# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)

        for i in range(3 , len(tasks) , 4):
            tasks[i] += processorTime[((i+1)//4) -1]
        
        return max(tasks)

        

        