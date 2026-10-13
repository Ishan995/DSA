class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        curr_sum=0
        prefix_sum={0:1}
        n=len(nums)
        for i in range(n):
            curr_sum+=nums[i]
            if (curr_sum-k) in prefix_sum:
                res+=prefix_sum[curr_sum-k]
            prefix_sum[curr_sum]=prefix_sum.get(curr_sum,0)+1
        return res
        
        
        