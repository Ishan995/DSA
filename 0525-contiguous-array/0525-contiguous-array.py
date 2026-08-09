class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        zero=0
        one=0
        res=0
        f={}
        for i in range (n):
            if nums[i]==0:
                zero+=1
            else:
                one+=1
            diff=zero-one
            if diff==0:
                res = max(res,i+1)
                continue
            if diff not in f:
                f[diff]=i
            else:
                length=i-f[diff]
                res=max(res,length)
        return res
