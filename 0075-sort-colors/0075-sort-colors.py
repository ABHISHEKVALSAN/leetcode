class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z_count = 0
        o_count = 0
        t_count = 0
        n = len(nums)
        for num in nums:
            if num==0:
                z_count+=1
            elif num==1:
                o_count+=1
            elif num==2:
                t_count+=1
        i = 0
        while i<n:
            if i < z_count:
                nums[i]=0
            elif i<z_count+o_count:
                nums[i]=1
            elif i< z_count+o_count+t_count:
                nums[i]=2
            i+=1