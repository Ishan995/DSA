class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[[-1 for _ in range(2)]for _ in range (n)]
        def fun(a,n,i,free):
            if i==n:
                return 0
            if dp[i][free]!=-1:
                return dp[i][free]
            if free==0:
                dp[i][free]=fun(a,n,i+1,1)
                return dp[i][free]
            c1=a[i]+fun(a,n,i+1,0)
            c2=fun(a,n,i+1,1)
            dp[i][free]=max(c1,c2)
            return dp[i][free]
        return fun(nums,n,0,1)
        

        
        