class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        total_sum=0
        curr_min,curr_max=0,0
        best_max=float('-inf')
        best_min=float('inf')

        for i in range(n):
            total_sum+=nums[i]
            curr_max=max(curr_max+nums[i],nums[i])
            best_max=max(best_max,curr_max)
            curr_min=min(curr_min+nums[i],nums[i])
            best_min=min(best_min,curr_min)
            
        if best_max < 0:
            return best_max

        return max(best_max,total_sum-best_min)
