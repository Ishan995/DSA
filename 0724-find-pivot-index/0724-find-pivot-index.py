class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        left=0
        n=len(nums)
        for i in range (n):
            if i>0:
                left+=nums[i-1]
            right=total-nums[i]-left
            if left==right:
                return i
        return -1
           
           

        