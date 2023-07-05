class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        i = 0
        j = n-1
        mw = 0
        while i < j:
            mw = max(mw,min(height[i],height[j])*(j-i))
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return mw
