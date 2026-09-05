class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix) * len(matrix[0]) - 1
        while i <= j:
            mid = (i + j) // 2
            row, col = self.get_actual_index(mid, matrix)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                j = mid - 1
            else:
                i = mid + 1
        return False

    def get_actual_index(self, num, matrix):
        row = num // len(matrix[0])
        col = num % len(matrix[0])
        return (row, col)