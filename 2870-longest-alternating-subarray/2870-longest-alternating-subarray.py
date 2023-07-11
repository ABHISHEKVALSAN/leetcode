class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        max_len = -1
        i = 1
        curr_len = 0
        sign = -1
        while i<n:
            #print('->',nums[i-1],nums[i])
            if (nums[i-1] - nums[i])==sign:
                #print(nums[i-1],nums[i])
                curr_len = 2
                sign*=-1
                i+=1
                while i<n and (nums[i-1]-nums[i])==sign:
                    #print('-',nums[i-1],nums[i])
                    sign*=-1
                    curr_len+=1
                    i+=1
                i-=1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 0
                sign = -1
                i+=1
        return max_len