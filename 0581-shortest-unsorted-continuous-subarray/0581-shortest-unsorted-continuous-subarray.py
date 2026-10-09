class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        if nums == sorted(nums):
            return 0

        sorted_nums = sorted(nums)
        l, r = 0, n - 1
        
        while l <= r and nums[l] == sorted_nums[l]:
            l += 1 
        while l <= r and nums[r] == sorted_nums[r]:
            r -= 1    
        return r - l + 1
 
        
        
        



        