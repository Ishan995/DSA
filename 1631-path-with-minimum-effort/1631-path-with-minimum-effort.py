class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        a=heights
        n=len(a)
        m=len(a[0])

        x=[-1,1,0,0]
        y=[0,0,-1,1]

        def valid(i,j,n,m):
            if i<0 or i>=n or j<0 or j>=m:
                return False
            return True 

        res=[[float('inf')for _ in range(m)]for _ in range(n)]

        pq=[]
        res[0][0]=0
        heapq.heappush(pq,(0,0,0)) #(dist,row,col)
        while pq:
            dist,row,col=heapq.heappop(pq)
            if dist>res[row][col]:
                continue
            for k in range(4):
                r=row+x[k]
                c=col+y[k]
                if not valid(r,c,n,m):
                    continue
                absdiff=abs(a[row][col]-a[r][c])
                newwt=max(dist,absdiff)
                if newwt<res[r][c]:
                    res[r][c]=newwt
                    heapq.heappush(pq,(newwt,r,c))
        return res[n-1][m-1]
                
           