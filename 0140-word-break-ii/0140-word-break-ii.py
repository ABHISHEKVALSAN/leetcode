class Solution:
    def solve(self, s, wordDict, max_len, min_len):
        if len(s)<min_len:
            yield "", False
        else:
            if s in wordDict:
                yield s, True
            for i in range(min_len,max_len+1):
                if s[:i] in wordDict:
                    for word, status in self.solve(s[i:], wordDict, max_len, min_len):
                        if status==True:
                            yield s[:i]+" "+word, True
            yield "", False


    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        max_len = 0
        min_len = 11
        for word in wordDict:
            max_len = max(max_len, len(word))
            min_len = min(min_len, len(word))
        result = []
        for word, status in self.solve(s, wordDict, max_len, min_len):
            if status==True:
                result.append(word)
        return result
        
