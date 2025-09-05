class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        res = 0
        for key in freq:
            if key + 1 in freq:
                res = max(res, freq[key] + freq[key + 1])
        
        return res