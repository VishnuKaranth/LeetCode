class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if(flowerbed[i] == 0 and n > 0):
                left = (i == 0) or flowerbed[i-1] == 0
                right = (i == len(flowerbed)-1) or flowerbed[i+1] == 0
                if left and right:
                    flowerbed[i] = 1
                    n = n-1
                i = i+1
        return n == 0