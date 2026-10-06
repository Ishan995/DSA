class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res=0
        for i in range (len(nums)):
            res=res^nums[i]
        return res
        