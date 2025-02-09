# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
            row = len(mat)
            matrix = mat
            count = 0
            for k in range(4):
                if matrix == target:
                    return True
                else:
                    swapped = [[0]*row for _ in range(row)]
                    for i in range(row):
                        for j in range(row):
                            swapped[j][row-i-1] = matrix[i][j]

                    matrix = swapped
                    print(matrix)
                    
            return False
                     