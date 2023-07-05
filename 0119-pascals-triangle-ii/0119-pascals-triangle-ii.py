class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex
        prev = 1
        row = [1]
        for i in range(n):
            curr = (prev * (n-i))//(i+1)
            row.append(curr)
            prev = curr
        return row