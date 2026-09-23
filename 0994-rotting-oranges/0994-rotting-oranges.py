class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int: 

        a=grid
        n=len(a)
        m=len(a[0])

        x=[-1,1,0,0]
        y=[0,0,-1,1]

        def valid(i,j,n,m):
            if i<0 or i>=n or j<0 or j>=m:
                return False
            return True

        q=deque()
        fresh=0
        time=0

        for i in range (n):
            for j in range(m):
                if a[i][j]==2:
                    q.append((i,j))
                    a[i][j]=-2
                elif a[i][j]==1:
                    fresh+=1

        while q and fresh>0:
            time+=1
            for _ in range(len(q)):
                r,c=q.popleft()
                for k in range(4):
                    row=r+x[k]
                    col=c+y[k]
                    if valid(row,col,n,m) and a[row][col]==1:
                        q.append((row,col))
                        a[row][col]=-2
                        fresh-=1

        if fresh >0:
            return -1
        return time


    



        