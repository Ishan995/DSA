class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a=nums1
        b=nums2
        if len(a)>len(b):
            a,b=b,a
        total=len(a)+len(b)
        half=total//2
        
        low=-1
        high=len(a)
        while low<=high:
            i=(low+high)//2
            j=half-i-2

            aleft=a[i] if i>=0 else float("-inf")
            aright=a[i+1] if i+1<len(a) else float("inf")
            bleft=b[j] if j>=0 else float("-inf")
            bright=b[j+1] if j+1<len(b) else float("inf")

            if aleft<=bright and bleft<=aright:
                if total%2!=0:
                    return min(aright,bright)
                return (max(aleft,bleft)+min(aright,bright)) / 2
            elif aleft>bright:
                high=i-1
            else:
                low=i+1


        