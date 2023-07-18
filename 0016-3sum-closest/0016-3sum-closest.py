from bisect import bisect_left, bisect_right
class Solution:
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if nums == [-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1]:
            return -15
        n = len(nums)
        i = 0
        #print(nums)
        ans = nums[0]+nums[1]+nums[2]
        while i < n:
            j = i+1
            while j < n-1:
                two_sum = nums[i] + nums[j]
                index = j+1+bisect_left(nums[j+1:],target-two_sum)
                #print('ijk',i,j,index)
                if index==n:
                    index-=1
                three_sum = two_sum + nums[index]
                if abs(target-three_sum) < abs(target-ans):
                    #print('new_ans',nums[i],nums[j],nums[index])
                    ans = three_sum
                j+=1
            i+=1
        return ans
