class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts=[0]+sorted(cuts)+[n]
        s=len(cuts)

        dp=[[-1 for _ in range(s)]for _ in range(s)]

        def fun(i,j):
            if i>j:
                return 0
        
            if dp[i][j]!=-1:
                return dp[i][j]

            res=float('inf')
            
            for k in range(i,j+1):
                cost=cuts[j+1]-cuts[i-1]
                r=cost+fun(i,k-1)+fun(k+1,j)
                if r<res:
                    res=r
            dp[i][j]=res
            return dp[i][j]

        return fun(1,s-2)
            
        
        