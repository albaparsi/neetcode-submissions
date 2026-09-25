class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        row1, col1 = len(matrix), len(matrix[0])
        l, r = 0, row1 * col1 - 1

        while l <= r:

            middle = l + (r - l) // 2
            row, col = middle // col1, middle % col1

            if target > matrix[row][col]:
                l = middle + 1

            elif target < matrix[row][col]:
                r = middle - 1

            elif target == matrix[row][col]:
                return True

        return False

        