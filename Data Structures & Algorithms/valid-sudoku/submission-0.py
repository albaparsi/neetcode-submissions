class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashColumn = {}
        hashRow = {}
        hashSquare = {}


        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue
                if r not in hashRow:
                    hashRow[r] = set()
                if val in hashRow[r]:
                    return False

                hashRow[r].add(val)

                if c not in hashColumn:
                    hashColumn[c] = set()
                if val in hashColumn[c]:
                    return False

                hashColumn[c].add(val)


                square = (r //3, c//3)

                if square not in hashSquare:
                    hashSquare[square]=set()

                if val in hashSquare[square]:
                    return False
                hashSquare[square].add(val)

        return True





        





        