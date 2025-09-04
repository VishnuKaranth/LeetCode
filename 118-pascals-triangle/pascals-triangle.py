class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for i in range(numRows):
            cur = [1] * (i + 1)

            for j in range(1, i):
                cur[j] = rows[i - 1][j - 1] + rows[i - 1][j]
            rows.append(cur)
        return rows