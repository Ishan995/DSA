class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        low=0
        high=n-1
        res=-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]<arr[mid+1]:
                low=mid+1
            else:
                res=mid
                high=mid-1
                
        return res