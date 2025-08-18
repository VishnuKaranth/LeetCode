class Solution:
    def reverseVowels(self, s: str) -> str:
        def is_vowel(ch):
            vowels = 'aeiouAEIOU'
            for v in vowels:
                if ch == v:
                    return True
            return False

        chars = []
        for ch in s:
            chars.append(ch)
        
        left = 0
        right = len(chars) - 1
        
        while left < right:
            while left < right and not is_vowel(chars[left]):
                left += 1
            while left < right and not is_vowel(chars[right]):
                right -= 1
            
            if left < right:
                temp = chars[left]
                chars[left] = chars[right]
                chars[right] = temp
                left += 1
                right -= 1

        result_chars = []
        for c in chars:
            result_chars.append(c)
        
        res_str = ""
        for ch in result_chars:
            res_str += ch
        
        return res_str