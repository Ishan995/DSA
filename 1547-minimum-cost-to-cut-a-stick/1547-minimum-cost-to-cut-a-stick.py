class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        # Step 1: Add boundary points 0 and n, then sort the cut positions.
        # Sorting is necessary so that cuts[j + 1] - cuts[i - 1] accurately represents
        # the current stick length for the range of cuts between indices i and j.
        cuts = [0] + sorted(cuts) + [n]
        s = len(cuts)

        # Step 2: Initialize a 2D matrix (s x s) with -1 using nested list comprehensions
        # to store memoized results and prevent redundant recursive calculations.
        dp = [[-1 for _ in range(s)] for _ in range(s)]

        def fun(i: int, j: int) -> int:
            # Base Case: No cuts left to process in this range (valid indices exhausted)
            if i > j:
                return 0
        
            # Step 3: Return cached result if already computed for subproblem (i, j)
            if dp[i][j] != -1:
                return dp[i][j]

            res = float('inf')
            
            # Step 4: Try making the cut at every available candidate index k from i to j
            for k in range(i, j + 1):
                # Cost of making a cut is the current length of the stick segment:
                # Right endpoint is cuts[j + 1] and left endpoint is cuts[i - 1]
                cost = cuts[j + 1] - cuts[i - 1]

                # Total cost = cost of current cut + min cost of left piece + min cost of right piece
                r = cost + fun(i, k - 1) + fun(k + 1, j)

                # Keep track of the minimum cost among all choices of k
                if r < res:
                    res = r

            # Step 5: Save minimum cost in dp table and return after trying all k values
            dp[i][j] = res
            return dp[i][j]

        # Step 6: Start processing for inner cuts (from index 1 to s - 2)
        # Index 0 is the left boundary (0) and index s - 1 is the right boundary (n)
        return fun(1, s - 2)

            
        
        