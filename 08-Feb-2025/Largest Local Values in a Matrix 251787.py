# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2): 
            for j in range(n-2): 
                ans[i][j] = max(grid[ii][jj] for ii in range(i, i+3) for jj in range(j, j+3))
        return ans 