class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        s = 0
        while i<n:
            j = i
            temp1 = nums[i]
            while True:
                temp2 = nums[(j+k)%n]
                nums[(j+k)%n] = temp1
                temp1 = temp2
                j = (j+k)%n 
                s+=1
                if j==i or s==n:
                    break
            if s==n:
                break
            i+=1
        print(nums)
