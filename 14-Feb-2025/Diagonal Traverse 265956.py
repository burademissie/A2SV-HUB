# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        row, col = len(mat), len(mat[0])
        r, c = 0, 0
        up = True
        answer = []

        for _ in range(row * col):
            answer.append(mat[r][c])

            if up:
                if c == col - 1: 
                    r += 1
                    up = False
                elif r == 0:  
                    c += 1
                    up = False
                else:  
                    r -= 1
                    c += 1
            else:
                if r == row - 1: 
                    c += 1
                    up = True
                elif c == 0: 
                    r += 1
                    up = True
                else: 
                    r += 1
                    c -= 1
                    
        return answer
