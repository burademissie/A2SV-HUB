# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrows = 1
        arrowpos = points[0][1]



        for xs , xe in points:
            if xs > arrowpos:
                arrows += 1
                arrowpos = xe

        return arrows
        