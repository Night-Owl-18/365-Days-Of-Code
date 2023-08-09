class Solution:
    def diagonalSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if m == 1: return matrix[0][0]
        c = 0
        for i in range(m):
            c += matrix[i][i]
            c += matrix[i][-1 - i]
        if m % 2 == 1: c -= matrix[m // 2][m // 2]

        return c
