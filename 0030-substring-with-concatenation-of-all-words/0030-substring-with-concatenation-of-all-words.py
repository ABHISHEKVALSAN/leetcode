class Solution:

    def is_substring(self,s: str,l: int,i: int,wd: dict):
        n = len(s)
        d = wd.copy()
        while i < n:
            curr_word = s[i:i+l]
            if curr_word in d.keys():
                if d[curr_word]==1:
                    d.pop(curr_word)
                else:
                    d[curr_word]-=1
            else:
                break
            i+=l
        if len(d)==0:
            return True
        return False

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        m = len(words)
        l = len(words[0])
        wd = {}
        for word in words:
            if word in wd.keys():
                wd[word]+=1
            else:
                wd[word] = 1

        result = []
        for i in range(n-l+1):
            if self.is_substring(s,l,i,wd):
                result.append(i)
        return result
