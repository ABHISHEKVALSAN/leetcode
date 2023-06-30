class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avg_arr = [-1 for _ in range(n)]
        if n < 2*k+1:
            return avg_arr
        ss = sum(nums[:2*k+1])
        i = k
        while i<n-k:
            avg_arr[i]=int(ss/(2*k+1))
            # print(ss)
            # print(avg_arr)
            ss = ss+nums[i+k+1]-nums[i-k] if i+k+1 < n else 0
            i+=1
        return avg_arr
