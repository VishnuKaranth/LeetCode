class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        pows = [1]
        while pows[-1] <= 10**9:
            pows.append(pows[-1] * 4)
        
        def prefix(n: int) -> int:
            if n <= 0:
                return 0
            total = 0
            for k in range(len(pows)-1):
                lo,hi = pows[k], pows[k+1] - 1
                if n < lo:
                    break
                total = total + (min(n, hi) - lo + 1) * (k + 1)
            return total

        ans = 0
        for l, r in queries:
            total_steps = prefix(r) - prefix(l-1)
            ans = ans + (total_steps + 1) // 2
        return ans