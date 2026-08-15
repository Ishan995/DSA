class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #find first position
        n=len(nums)
        low=0
        high=(n-1)
        first=-1

        while (low<=high):
            mid=(low+high)//2
            if nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                first=mid
                high=mid-1  #keep searching left

        #find last position
        n=len(nums)
        low=0
        high=(n-1)
        last=-1

        while (low<=high):
            mid=(low+high)//2
            if nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                last=mid
                low=mid+1  #keep searching right
        
        return [first,last]

            

        