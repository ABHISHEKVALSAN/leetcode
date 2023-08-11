class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        l = len(flowerbed)
        flowerbed = [0] + flowerbed + [0]
        for i in range(1,l+1):
            if flowerbed[i-1]==flowerbed[i+1]==flowerbed[i]==0:
                flowerbed[i]=1
                n-=1
                if n==0:
                    return True
        return False