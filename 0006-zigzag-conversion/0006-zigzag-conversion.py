class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        i = 0
        n = len(s)
        inc = True
        k = 0 
        result = ['' for _ in range(numRows)]
        while i<n:
            result[k]+=s[i]
            if inc:
                if k==numRows-1:
                    inc=False
                    k-=1
                else:
                    k+=1
            else:
                if k==0:
                    inc = True
                    k+=1
                else:
                    k-=1
            i+=1
        return ''.join(result)