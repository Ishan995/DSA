class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n=len(nums)
        res=[0]*n
        for i in range(n):
            res[i]=1
            for j in range(i):
                if nums[j]<nums[i]:
                    res[i]=max(res[i],res[j]+1)
        ans=1
        for i in range (n):
            ans=max(ans,res[i])
        return ans

     
  
        