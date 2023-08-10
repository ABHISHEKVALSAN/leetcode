class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        l = len(flowerbed)
        flowerbed = [0] + flowerbed + [0]
        fc = 0
        i = 1
        while i <= l:
            if flowerbed[i-1]==flowerbed[i+1]==flowerbed[i]==0:
                flowerbed[i]=1
                fc+=1
            i+=1
        return fc>=n