class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        res=-1

        while low<=high:
            guess=(low+high)//2
            if nums[guess]>nums[n-1]:   #(agar element part 2 mein hain)
                low=guess+1
            else:                       #(agar element part 1 mein ho)
                res=nums[guess]
                high=guess-1            # first occurence dhundne ke liye kyunki woh min

        return res

