class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1

        while low <= high:
            guess = (low + high) // 2

            # 1. Target found
            if nums[guess] == target:
                return guess

            # 2. If mid/guess is in Part 1
            if nums[guess] >= nums[0]:
                if nums[guess] < target:
                    low = guess + 1
                else:  # nums[guess] > target
                    if nums[0] > target:
                        low = guess + 1  # Target is in P2
                    else:
                        high = guess - 1  # Target is to the left in P1

            # 3. If mid/guess is in Part 2
            else:
                if nums[guess] > target:
                    high = guess - 1
                else:  # nums[guess] < target
                    if nums[n - 1] < target:
                        high = guess - 1  # Target is in P1
                    else:
                        low = guess + 1  # Target is to the right in P2

        return -1
        