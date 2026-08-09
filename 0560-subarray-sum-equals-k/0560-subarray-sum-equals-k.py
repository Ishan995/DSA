class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        curr_sum=0
        seen_sum={0:1}
        n=len(nums)
        for i in range(n):
            curr_sum+=nums[i]
            if (curr_sum-k) in seen_sum:
                count+=seen_sum[curr_sum-k]
            seen_sum[curr_sum]=seen_sum.get(curr_sum,0)+1
        return count
        
        
        