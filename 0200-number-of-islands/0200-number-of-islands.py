class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        a=grid
        n=len(a)
        m=len(a[0])

        vis=[[False for _ in range(m)]for _ in range(n)]

        x=[-1,1,0,0]
        y=[0,0,-1,1]

        def valid(i,j,n,m):
            if i<0 or i>=n or j<0 or j>=m:
                return False
            return True 
        
        def dfs(i,j):
            vis[i][j]=True
            for k in range(4):
                row=i+x[k]
                col=j+y[k]
                
                if valid(row,col,n,m) and a[row][col]=='1' and vis[row][col]==False:
                    dfs(row,col)
        
        res=0
        for i in range(n):
            for j in range(m):
                if a[i][j]=='1' and vis[i][j]==False:
                    dfs(i,j)
                    res+=1
        return res

        



       