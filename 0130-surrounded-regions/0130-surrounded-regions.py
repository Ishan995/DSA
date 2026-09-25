class Solution:
    def solve(self, board: list[list[str]]) -> None:
        a=board
        n=len(a)
        m=len(a[0])

        x=[-1,1,0,0]
        y=[0,0,-1,1]

        def valid(i,j,n,m):
            if i<1 or i>=n or j<0 or j>=m:
                return False
            return True
        
        def dfs(i,j):
            a[i][j]='#' #visited
            for k in range (4):
                row=i+x[k]
                col=j+y[k]
                if valid(row,col,n,m) and a[row][col]=='O':
                    dfs(row,col)
        
        #first row 
        for j in range(m):
            if a[0][j]=='O':
                dfs(0,j)

        #last row
        for j in range (m):
            if a[n-1][j]=='O':
                dfs(n-1,j)

        #first col
        for i in range (n):
            if a[i][0]=='O':
                dfs(i,0)

        #last col
        for i in range(n):
            if a[i][m-1]=='O':
                dfs(i,m-1)

        for i in range(n):
            for j in range (m):
                if a[i][j]=='#':
                    a[i][j]='O'
                elif a[i][j]=='O':
                    a[i][j]='X'







        
        
       
        