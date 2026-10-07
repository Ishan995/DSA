class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n=len(nums)
        reach=0
        for i in range(n):
            if reach<i:
                return False
            reach=max(reach,i+nums[i])
            if reach>=n-1:
                return True 
        return True
        