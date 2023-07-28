class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2': 'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno', 
            '7': 'pqrs', '8':'tuv', '9': 'wxyz'
        }
        def solve(num):
            if len(num)==1:
                for ch in d[num]:
                    yield ch
            elif len(num)>1:
                for ch in d[num[0]]:
                    for ans in solve(num[1:]):
                        yield ch + ans
        result = []
        for ch in solve(digits):
            result.append(ch)
        return result