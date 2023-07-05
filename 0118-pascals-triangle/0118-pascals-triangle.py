class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1,numRows+1):
            if i==1:
                result.append([1])
            elif i==2:
                result.append([1,1])
            else:
                temp =[1]
                n = len(result[-1])
                i = 0
                while i < n-1:
                    temp.append(result[-1][i]+result[-1][i+1])
                    i+=1
                temp.append(1)
                result.append(temp)
        return result
