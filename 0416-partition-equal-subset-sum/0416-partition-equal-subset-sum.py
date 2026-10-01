class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum=sum(nums)
        if total_sum%2!=0: #for odd no no equal parts
            return False

        target=total_sum//2
        n=len(nums)
        dp=[[-1 for _ in range(target+1)] for _ in range(n+1)]

        for j in range(target+1):
            dp[n][j]=0
        dp[n][0]=1

        for i in range(n-1,-1,-1):
            for j in range(target+1):
                if nums[i]>j:
                    dp[i][j]=dp[i+1][j]
                else:
                    dp[i][j]=dp[i+1][j-nums[i]] or dp[i+1][j]
        return bool(dp[0][target])



        