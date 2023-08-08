class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_one(num):
            count = 0
            while num:
                num &= num-1
                count+=1
            return count
        i = 0
        result = []
        while i <= n:
            result.append(count_one(i))
            i+=1
        return result
