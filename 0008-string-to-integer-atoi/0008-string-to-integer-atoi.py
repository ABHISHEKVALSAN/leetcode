class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if ' ' in s:
            s = s.split(' ')[0]
        if '.' in s:
            s = s.split('.')[0]
        print(s)
        if len(s)==0:
            return 0
        sign = 1 if s[0] in '1234567890+' else -1
        if s.startswith('-') or s.startswith('+'):
            s = s[1:]
        if len(s)==0 or s[0] not in '1234567890':
            return 0
        tzi = 0
        while tzi < len(s) and s[tzi]=='0':
            tzi+=1
        nei = tzi
        while nei < len(s) and s[nei] in '1234567890':
            nei+=1
        s = s[tzi:nei]
        if len(s)==0:
            return 0
        print(s)
        if len(s)>10:
            if sign==-1:
                return -2**31
            else:
                return 2**31-1
        if sign==-1:
            return max(int(s)*sign,-2**31)
        if sign==1:
            return min(int(s)*sign,2**31-1)*sign