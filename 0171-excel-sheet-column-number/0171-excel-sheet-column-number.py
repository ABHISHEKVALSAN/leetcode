class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alp = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        d = {e:i for i,e in enumerate(alp)}
        arr = list(columnTitle)[::-1]
        curr = 0
        while arr:
            ch = arr.pop()
            curr = curr * 26 + d[ch]+1
        return curr

