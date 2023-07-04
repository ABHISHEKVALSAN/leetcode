class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        one = 0
        two = 0
        for num in nums:
            print(bin(one),bin(num),bin(~two))
            one = (one ^ num) & ~two
            print(bin(two),bin(num),bin(~one))
            two = (two ^ num) & ~one
        return one
        