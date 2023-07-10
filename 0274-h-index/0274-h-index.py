class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        h_ind = 0
        for i, c in enumerate(citations):
            if i+1<=c:
                h_ind+=1
        return h_ind