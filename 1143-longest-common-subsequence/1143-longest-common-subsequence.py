class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n=len(s1)
        m=len(s2)
        dp=[[-1 for _ in range(m+1)] for _ in range(n+1)]

        for j in range(m+1):
            dp[n][j]=0
        for i in range(n+1):
            dp[i][m]=0
    
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if s1[i]==s2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]


   