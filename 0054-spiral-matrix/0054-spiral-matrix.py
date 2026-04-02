class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        row_start,row_end=0,n-1
        col_start,col_end=0,m-1
        ans=[]

        while len(ans) < n*m:
            # row_start:col_start->col_end
            for i in range(col_start,col_end+1):
                ans.append(matrix[row_start][i])
            row_start+=1
            if len(ans)==n*m:
                break

            # col_end:row_start->row_end
            for i in range(row_start,row_end+1):
                ans.append(matrix[i][col_end])
            col_end-=1
            if len(ans)==n*m:
                break

            # row_end:col_end->col_start
            for i in range(col_end,col_start-1,-1):
                ans.append(matrix[row_end][i])
            row_end-=1
            if len(ans)==n*m:
                break

            # col_start:row_end->row_start
            for i in range(row_end,row_start-1,-1):
                ans.append(matrix[i][col_start])
            col_start+=1

        return ans