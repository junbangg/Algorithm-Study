# Two Pointer Approach
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False


# Pythonic Solution
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    return any(target in row for row in matrix)

