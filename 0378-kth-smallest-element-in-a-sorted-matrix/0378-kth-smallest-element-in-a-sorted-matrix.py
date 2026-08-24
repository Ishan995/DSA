class Solution:
    def fun(self, a: list[list[int]], n: int, m: int, guess: int) -> int:
        row = n - 1
        col = 0
        count = 0

        while row >= 0 and col < m:
            if a[row][col] <= guess:
                count = count + row + 1
                col += 1
            else:
                row -= 1

        return count

    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        a = matrix
        n = len(a)
        m = len(a[0])

        low = a[0][0]
        high = a[n - 1][m - 1]
        res = -1

        while low <= high:
            guess = (low + high) // 2
            ans = self.fun(a, n, m, guess)

            if ans < k:
                low = guess + 1
            else:
                res = guess
                high = guess - 1

        return res