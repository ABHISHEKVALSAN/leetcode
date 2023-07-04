class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        c = 0
        i = n-1
        while i >= 0:
            if digits[i]==9:
                digits[i]=0
                i-=1
                c = 1
            else:
                digits[i]+=1
                c = 0
                break
        print(digits)
        if c==1:
            result = [1]
            for i in digits:
                result.append(i)
            return result
        return digits