class Solution:
    def jump(self, nums: List[int]) -> int:
        MAX_INT = 10**9
        n = len(nums)
        if n==1:
            return 0
        jump_count = [MAX_INT for _ in range(n)]
        jump_count[-1] = 0
        i = n-2
        while i>=0:
            if nums[i]+i >= n-1:
                jump_count[i] = 1
            else:
                j = nums[i]
                min_jump = MAX_INT
                while j > 0:
                    min_jump = min(min_jump, jump_count[i+j])
                    if min_jump==1:
                        break
                    j-=1
                jump_count[i] = min_jump+1
            i-=1
        print(jump_count)
        return jump_count[0]