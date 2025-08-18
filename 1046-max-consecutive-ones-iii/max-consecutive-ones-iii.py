class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_ = 0
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count = count + 1
            while count > k:
                if nums[l] == 0:
                    count = count - 1
                l = l + 1
            size = i - l + 1
            if size > max_:
                max_ = size
        return max_