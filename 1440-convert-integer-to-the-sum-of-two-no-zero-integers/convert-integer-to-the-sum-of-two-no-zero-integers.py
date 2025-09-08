class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for first_num in range(1, n):
            second_num = n - first_num
            combined_str = str(first_num) + str(second_num)
            if '0' not in combined_str:
                return [first_num, second_num]