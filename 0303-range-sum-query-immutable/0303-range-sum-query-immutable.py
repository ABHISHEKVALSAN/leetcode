class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_array = [0]
        s = 0
        for num in nums:
            s+=num
            self.sum_array.append(s)


    def sumRange(self, left: int, right: int) -> int:
        return self.sum_array[right+1] - self.sum_array[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)