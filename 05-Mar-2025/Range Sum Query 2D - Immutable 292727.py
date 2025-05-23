# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.sumMat = [[0] * (col + 1) for _ in range(row+1)]

        for r in range(row):
            prefix = 0
            for c in range(col):
                prefix += matrix[r][c]
                higher = self.sumMat[r][c + 1]

                self.sumMat[r+1][c+1] = prefix + higher

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 , row2 , col1 , col2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        botright = self.sumMat[row2][col2]
        topleft = self.sumMat[row1-1][col1-1]
        higher = self.sumMat[row1-1][col2]
        left = self.sumMat[row2][col1-1]

        return botright - higher - left + topleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)