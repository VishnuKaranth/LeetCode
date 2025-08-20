class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        total_count = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        left = dp[i][j-1]
                        top = dp[i-1][j]
                        diagonal = dp[i-1][j-1]

                        min_val = left
                        if top < min_val:
                            min_val = top
                        if diagonal < min_val:
                            min_val = diagonal
                        
                        dp[i][j] = min_val + 1
                total_count = total_count + dp[i][j]

        return total_count
                    
