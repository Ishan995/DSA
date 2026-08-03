class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        window_sum = 0
        res = float('inf')

        for r in range(n):
            window_sum += nums[r]

            while window_sum >= target:
                res = min(res, r - l + 1)
                window_sum -= nums[l]   
                l += 1

        return 0 if res == float('inf') else res