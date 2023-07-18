class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n==0:
            return []
        first = nums[0]
        last = nums[0]
        result = []
        i = 1
        
        while i<n:
            if nums[i]==last+1:
                last = nums[i]
            else:
                if first==last:
                    result.append(f"{first}")
                else:
                    result.append(f"{first}->{last}")
                first = nums[i]
                last = nums[i]
            i+=1
        if first==last:
            result.append(f"{first}")
        else:
            result.append(f"{first}->{last}")     
        return result