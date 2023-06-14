class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lp = strs[0]
        ss_len = len(strs[0])
        if ss_len==0:
            return ''
        for string in strs[1:]:
            print(string)
            if len(string)==0:
                return ''
            ss_len = min(ss_len, len(string))
            for i, ch in enumerate(string):
                if i >= len(lp):
                    break
                if lp[i]!=ch:
                    print(ss_len,i)
                    ss_len = min(ss_len,i)
                    break
        if ss_len==0:
            return ''
        return lp[:ss_len]
        
            