class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(0, 61):
            target = num1 - i * num2
            if target.bit_count() <= i <= target:
                return i
        return -1