class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def solve(matrix,i,j,d):
            r,c= len(matrix),len(matrix[0])
            i = 0
            j = 0
            dc = 0
            while True:
                if dc>=10:
                    break
                if dc==0 and matrix[i][j]!=-101:
                    yield matrix[i][j]
                    matrix[i][j]=-101
                if d==0:
                    if j<c-1 and matrix[i][j+1]!=-101:
                        j+=1
                        dc=0
                    else:
                        dc+=1
                        d = (d+1)%4
                    continue
                elif d==1:
                    if i<r-1 and matrix[i+1][j]!=-101:
                        i+=1
                        dc=0
                    else:
                        dc+=1
                        d = (d+1)%4
                elif d==2:
                    if j>0 and matrix[i][j-1]!=-101:
                        j-=1
                        dc=0
                    else:
                        dc+=1
                        d = (d+1)%4
                elif d==3:
                    if i>0 and matrix[i-1][j]!=-101:
                        i-=1
                        dc=0
                    else:
                        dc+=1
                        d = (d+1)%4

        r,c = len(matrix),len(matrix[0])
        ans = []
        for element in solve(matrix,0,0,0):
            ans.append(element)
        return ans
        
        
