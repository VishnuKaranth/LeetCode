class Solution:
    def C2(self, x: int) -> int:
        return (x * (x - 1)) // 2 if x >= 2 else 0
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > 3 * limit:
            return 0
        
        total = self.C2(n + 2)
        subt = 3 * self.C2(n - limit + 1)
        addb = 3 * self.C2(n - 2 *limit)
        return total - subt + addb