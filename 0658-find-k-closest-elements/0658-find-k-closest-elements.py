class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low=0
        high=len(arr)-k-1
        while low<=high:
            mid=(low+high)//2
            if x-arr[mid]>arr[mid+k]-x:
                low=mid+1
            else:
                high=mid-1
        return arr[low:low+k]