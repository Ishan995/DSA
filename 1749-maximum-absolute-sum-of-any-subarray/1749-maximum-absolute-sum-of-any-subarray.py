class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_min=curr_max=0
        min_sum=float('inf')
        max_sum=float('-inf')

        for i in range(len(nums)):
            curr_min=min(curr_min+nums[i],nums[i])
            min_sum=min(min_sum,curr_min)
            curr_max=max(curr_max+nums[i],nums[i])
            max_sum=max(max_sum,curr_max)

        return max(abs(min_sum),abs(max_sum))
        

       