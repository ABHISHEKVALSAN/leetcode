class Solution:
    def valid_string(self,s):
        n = 0
        for i in s:
            if i == '0':
                n+=1
            elif i == '1':
                n-=1
            if n<0:
                return False
        if n==0:
            print(s,'t')
            return True
        else:
            return False

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        for i in range(0,2**(n*2)):
            string = bin(i)[2:].zfill(n*2)
            if self.valid_string(string):
                string = string.replace('0','(')
                string = string.replace('1',')')
                ans.append(string)
        return ans

