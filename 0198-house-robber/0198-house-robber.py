class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[[-1 for _ in range(2)]for _ in range (n)]
        def fun(i,free):
            if i==n:
                return 0
            if dp[i][free]!=-1:
                return dp[i][free]
            if free==0:
                dp[i][free]=fun(i+1,1)
                return dp[i][free]
            c1=nums[i]+fun(i+1,0)
            c2=fun(i+1,1)
            dp[i][free]=max(c1,c2)
            return dp[i][free]
        return fun(0,1)
        

        
        