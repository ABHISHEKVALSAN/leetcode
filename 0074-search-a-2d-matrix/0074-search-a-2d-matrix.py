class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix) , len(matrix[0])
        first = 0
        last = row*col-1
        while first <= last:
            mid = (first+last)//2
            i , j = mid//col, mid%col
            if matrix[i][j]==target:
                return True
            elif matrix[i][j] < target:
                first = mid + 1
            else:
                last = mid - 1
        return False