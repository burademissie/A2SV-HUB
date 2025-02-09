# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        subg = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                if board[i][j] == ".":
                    continue

                subi = (i//3) * 3 + j//3
                
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in subg[subi]:
                    return False
            
                row[i].add(board[i][j])
                
                col[j].add(board[i][j])

                subg[subi].add(board[i][j])

        return True


        