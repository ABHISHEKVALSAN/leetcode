class Solution:
    def rob(self, nums: List[int]) -> int:
        best = {}
        def helper(index):

            if index >= len(nums):
                return 0
            if index in best:
                return best[index]
            
            total = max(helper(index+2),helper(index+3))

            best[index] = total + nums[index]


            return total + nums[index]

        
        return max(helper(0),helper(1))
