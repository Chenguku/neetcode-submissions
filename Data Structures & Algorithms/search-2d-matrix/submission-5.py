class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        dim_x = len(matrix[0])
        dim_y = len(matrix)

        l, r = 0, dim_x * dim_y - 1
        while r >= l:
            m = (r + l) // 2
            if matrix[m // dim_x][m % dim_x] == target:
                return True
            elif matrix[m // dim_x][m % dim_x] < target:
                l = m + 1
            elif matrix[m // dim_x][m % dim_x] > target:
                r = m - 1
        return False