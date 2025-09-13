class Solution:
    def maxFreqSum(self, s: str) -> int:
        frq = {}

        for ch in s:
            if ch in frq:
                frq[ch] += 1
            else:
                frq[ch] = 1

        vowel_cnt = 0
        const_cnt = 0

        for ch in frq:
            if ch in 'aeiouAEIOU':
                if frq[ch] > vowel_cnt:
                    vowel_cnt = frq[ch]
            else:
                if frq[ch] > const_cnt:
                    const_cnt = frq[ch]
        
        return vowel_cnt + const_cnt
