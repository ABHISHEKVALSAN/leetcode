class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        i = 0 
        n = len(nums)

        i=0
        while i < n and nums[i]==1:
            i+=1
        if i==n:
            return n-1

        i=0
        while i < n and nums[i]!=1:
            i+=1
        if i==n:
            return 0
        
        curr = nums[i]
        sub_arr = [1]
        for num in nums[i+1:]:
            if num==curr:
                sub_arr[-1]+=1
            else:
                sub_arr.append(1)
                curr = num
        i = 0
        ans = 0
        print(sub_arr)
        n = len(sub_arr)
        while i < n:
            if i==n-1:
                ans = max(ans, sub_arr[i])
            else:
                if i!=n-2 and sub_arr[i+1]==1:
                    ans = max(ans, sub_arr[i]+sub_arr[i+2])
                else:
                    ans = max(ans, sub_arr[i])
            i+=2
        return ans