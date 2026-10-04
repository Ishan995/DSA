class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        #k=k*2 (no of trans)
        a = prices
        n = len(a)
        if n == 0 or k == 0:
            return 0

        k = k * 2

        dp = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]

        for j in range(k + 1):
            dp[n][j] = 0

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(n - 1, -1, -1):
            for j in range(1, k + 1):
                if j % 2 == 0:  # buy state because first you can only buy
                    yes = dp[i + 1][j - 1] - a[i]
                    no = dp[i + 1][j]
                    dp[i][j] = max(yes, no)
                else:  # sell state
                    yes = dp[i + 1][j - 1] + a[i]
                    no = dp[i + 1][j]
                    dp[i][j] = max(yes, no)

        return dp[0][k]
        