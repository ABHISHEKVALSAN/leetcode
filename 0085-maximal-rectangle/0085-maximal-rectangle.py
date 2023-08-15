class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maximum_rect_histogram(arr):
            arr.append(0)
            stack = [-1]
            mx_area = 0
            for i, height in enumerate(arr):
                while int(height) < int(arr[stack[-1]]):
                    l = int(arr[stack.pop()])
                    b = i - stack[-1] - 1
                    mx_area = max(mx_area, l*b)
                stack.append(i)
            return mx_area
        row, col = len(matrix),len(matrix[0])
        for i in range(1,row):
            for j in range(col):
                if matrix[i][j]=='1':
                    matrix[i][j] = str(int(matrix[i][j]) + int(matrix[i-1][j]))
        mx_rect_area = 0
        for row in matrix:
            mx_rect_area = max(mx_rect_area, maximum_rect_histogram(row))
        print(matrix)
        return mx_rect_area

        