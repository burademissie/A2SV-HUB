# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i=0
        j=0

        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            if end1 >= start2 and end2 >= start1:
                start3 = max(start1, start2)
                end3 = min(end1, end2)
                res.append([start3,end3])

            if end1 < end2:
                i += 1
            else:
                j += 1

        return res