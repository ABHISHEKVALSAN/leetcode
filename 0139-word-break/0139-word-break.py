class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def solve(word):
            if word in record:
                return record[word]
            if word in wordDict:
                record[word]=True
                return True
            if not word:
                return True
            for w in wordDict:
                if word.startswith(w):
                    new_word = word[len(w):]
                    if solve(new_word):
                        record[word]=True
                        return True
            record[word]=False
            return False
        record = {}
        return solve(s)