class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum=sum(nums)
        if (total_sum+target)%2!=0 or abs(target)>total_sum:
            return 0
        pos=(total_sum+target)//2
        n=len(nums)
        dp=[[-1 for _ in range(pos+1)] for _ in range(n+1)]
        for j in range(pos+1):
            dp[n][j]=0
        dp[n][0]=1
        for i in range(n-1,-1,-1):
            for j in range(pos+1):
                if nums[i]>pos:
                    dp[i][j]=dp[i+1][j]
                else:
                    dp[i][j]=dp[i+1][j-nums[i]]+dp[i+1][j]
        return dp[0][pos]


        