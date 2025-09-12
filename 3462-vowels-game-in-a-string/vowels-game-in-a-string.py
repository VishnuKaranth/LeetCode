class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiou")
        vowel_count = sum(1 for ch in s if ch in vowels)
        return vowel_count > 0        