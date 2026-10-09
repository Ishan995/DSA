class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        sorted_nums=sorted(nums)
        n=len(nums)
        l=0
        r=n-1

        while l<=r:
            if nums[l]!=sorted_nums[l]:
                break
            l+=1
        
        while l<=r:
            if nums[r]!=sorted_nums[r]:
                break
            r-=1
        
        if l>r:
            return 0
        
        return r-l+1
        
        
        



        