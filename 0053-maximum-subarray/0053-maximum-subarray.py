class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        bestending=nums[0]
        ans=nums[0]

        for i in range(1,n):
            v1 = bestending + nums[i]
            v2 = nums[i]
            bestending = max(v1,v2)
            ans =  max(ans,bestending)

        return ans
        

        