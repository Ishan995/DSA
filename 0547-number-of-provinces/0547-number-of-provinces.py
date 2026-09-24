class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        a=isConnected
        n=len(a)

        vis = [False for _ in range (n)]

        def dfs(i):
            vis[i]=True
            for j in range(n):
                if a[i][j]==1 and vis[j]==False:
                    dfs(j)

        provinces=0
        for k in range(n):
            if vis[k]==False:
                dfs(k)
                provinces+=1
        return provinces


    



        