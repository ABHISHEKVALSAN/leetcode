class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=1:
            return 0
        if n==2:
            return abs(nums[0]-nums[1])
        mi = min(nums)
        mx = max(nums)
        pivot = -1
        for num in nums:
            if num!=mi and num!=mx:
                pivot = num
                break
        if pivot==-1:
            return abs(mi-mx)
        l = []
        l_max = -1
        for num in nums:
            if num<=pivot:
                l.append(num)
                l_max = max(l_max,num)
        m = []
        m_min = 10**9+1
        for num in nums:
            if num>pivot:
                m.append(num)
                m_min = min(m_min,num)
        max_gap = max(self.maximumGap(l),self.maximumGap(m),abs(l_max-m_min))
        return max_gap
