class Solution:
    def isHappy(self, n: int) -> bool:

        def find_square(n):
            total = 0
            while n:
                d = n % 10
                total += d * d
                n //= 10
            return total

        slow, fast = n, n

        while True:
            slow = find_square(slow)
            fast = find_square(find_square(fast))

            if slow == fast:
                break

        return slow == 1


        