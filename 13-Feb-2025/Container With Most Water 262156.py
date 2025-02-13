# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j = len(height)-1
        area=[]
        while i<j:
        
            a=(j-i)*min(height[i],height[j])
            area.append(a)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
            
        return max(area)

        