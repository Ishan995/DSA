class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        a=grid
        n=len(a)
        m=len(a[0])

        res=[[float('inf') for _ in range(m)]for _ in range(n)]

        x=[-1,1,0,0]
        y=[0,0,-1,1]

        def valid(i,j,n,m):
            if (i<0 or i>=n or j<0 or j>=m):
                return False
            return True
        
        pq=[]
        res[0][0]=a[0][0]
        heapq.heappush(pq,(a[0][0],0,0))
        while pq:
            dist,row,col=heapq.heappop(pq)
            if row==n-1 and col==m-1:
                return dist
            if dist>res[row][col]:
                continue
            for k in range (4):
                r=row+x[k]
                c=col+y[k]
                if not valid(r,c,n,m):
                    continue
                newwt=max(dist,a[r][c])
                if newwt<res[r][c]:
                    res[r][c]=newwt
                    heapq.heappush(pq,(newwt,r,c))
        
        return res[n-1][m-1]

                


        