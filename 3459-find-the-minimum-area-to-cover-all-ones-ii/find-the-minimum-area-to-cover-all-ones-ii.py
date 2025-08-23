class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ones = [(r, c) for r in range(n) for c in range(m) if grid[r][c] == 1]

        # Quick guard: problem guarantees at least three 1's
        if len(ones) < 3:
            return 0

        # Compute tight bounding box area of 1's within [r1..r2] x [c1..c2].
        # Returns (count, area). If count == 0, area is inf (invalid region).
        def bbox_area_in_region(r1, r2, c1, c2):
            minr, maxr = inf, -inf
            minc, maxc = inf, -inf
            cnt = 0
            for r, c in ones:
                if r1 <= r <= r2 and c1 <= c <= c2:
                    cnt += 1
                    if r < minr: minr = r
                    if r > maxr: maxr = r
                    if c < minc: minc = c
                    if c > maxc: maxc = c
            if cnt == 0:
                return 0, inf
            return cnt, (maxr - minr + 1) * (maxc - minc + 1)

        total_ans = inf

        # ----- Case A: three vertical strips -----
        # choose c1 < c2 as last columns of left and middle strips
        for c1 in range(0, m - 2):
            for c2 in range(c1 + 1, m - 1):
                cntL, areaL = bbox_area_in_region(0, n - 1, 0, c1)
                cntM, areaM = bbox_area_in_region(0, n - 1, c1 + 1, c2)
                cntR, areaR = bbox_area_in_region(0, n - 1, c2 + 1, m - 1)
                if cntL and cntM and cntR:
                    total_ans = min(total_ans, areaL + areaM + areaR)

        # ----- Case B: three horizontal strips -----
        for r1 in range(0, n - 2):
            for r2 in range(r1 + 1, n - 1):
                cntT, areaT = bbox_area_in_region(0, r1, 0, m - 1)
                cntM, areaM = bbox_area_in_region(r1 + 1, r2, 0, m - 1)
                cntB, areaB = bbox_area_in_region(r2 + 1, n - 1, 0, m - 1)
                if cntT and cntM and cntB:
                    total_ans = min(total_ans, areaT + areaM + areaB)

        # ----- Case C: one vertical cut, then split LEFT horizontally -----
        for c in range(0, m - 1):
            # Left side split into top/bottom; right side single
            for r in range(0, n - 1):
                cntLT, areaLT = bbox_area_in_region(0, r, 0, c)
                cntLB, areaLB = bbox_area_in_region(r + 1, n - 1, 0, c)
                cntR,  areaR  = bbox_area_in_region(0, n - 1, c + 1, m - 1)
                if cntLT and cntLB and cntR:
                    total_ans = min(total_ans, areaLT + areaLB + areaR)

        # ----- Case D: one vertical cut, then split RIGHT horizontally -----
        for c in range(0, m - 1):
            for r in range(0, n - 1):
                cntL,  areaL  = bbox_area_in_region(0, n - 1, 0, c)
                cntRT, areaRT = bbox_area_in_region(0, r, c + 1, m - 1)
                cntRB, areaRB = bbox_area_in_region(r + 1, n - 1, c + 1, m - 1)
                if cntL and cntRT and cntRB:
                    total_ans = min(total_ans, areaL + areaRT + areaRB)

        # ----- Case E: one horizontal cut, then split TOP vertically -----
        for r in range(0, n - 1):
            for c in range(0, m - 1):
                cntTL, areaTL = bbox_area_in_region(0, r, 0, c)
                cntTR, areaTR = bbox_area_in_region(0, r, c + 1, m - 1)
                cntB,  areaB  = bbox_area_in_region(r + 1, n - 1, 0, m - 1)
                if cntTL and cntTR and cntB:
                    total_ans = min(total_ans, areaTL + areaTR + areaB)

        # ----- Case F: one horizontal cut, then split BOTTOM vertically -----
        for r in range(0, n - 1):
            for c in range(0, m - 1):
                cntT,  areaT  = bbox_area_in_region(0, r, 0, m - 1)
                cntBL, areaBL = bbox_area_in_region(r + 1, n - 1, 0, c)
                cntBR, areaBR = bbox_area_in_region(r + 1, n - 1, c + 1, m - 1)
                if cntT and cntBL and cntBR:
                    total_ans = min(total_ans, areaT + areaBL + areaBR)

        return total_ans