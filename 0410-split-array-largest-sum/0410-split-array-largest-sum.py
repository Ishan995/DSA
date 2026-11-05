class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        res=0

        while low<=high:
            guess=(low+high)//2
            subarrays=1
            curSum=0
            for n in nums:
                if curSum+n>guess:
                    subarrays+=1
                    curSum=n
                else:
                    curSum+=n

            if subarrays<=k:
                res=guess
                high=guess-1
            else:
                low=guess+1
        return res