class Solution:
    def trap(self, height: List[int]) -> int:
        mh = 0
        mhi = 0
        n = len(height)
        for i,h in enumerate(height):
            if h > mh:
                mh = h
                mhi = i
        
        vol = 0
        i = 0
        l_max = 0
        while i < mhi:
            l_max = max(l_max,height[i])
            vol += max(0,l_max-height[i])
            i+=1

        r_max = 0
        j = n-1
        while j > mhi:
            r_max = max(r_max, height[j])
            vol += max(0,r_max-height[j])
            j-=1
        return vol