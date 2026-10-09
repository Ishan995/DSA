class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:

        sorted_nums = sorted(nums)
        l = 0
        r = len(nums) - 1

        while l < len(nums) and nums[l] == sorted_nums[l]:
            l += 1

        while r >= 0 and nums[r] == sorted_nums[r]:
            r -= 1

        if l >= r:
            return 0

        return r - l + 1

        
        



        