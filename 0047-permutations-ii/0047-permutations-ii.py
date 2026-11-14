class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        diary=[]
        n=len(nums)

        def fun():
            if len(diary)==n:
                res.append(diary.copy())
                return 
            
            for j in range(n):
                if j>0 and nums[j]==nums[j-1]:
                    continue
                if diary.count(nums[j])==nums.count(nums[j]):
                    continue
                diary.append(nums[j])
                fun()
                diary.pop()

        fun()
        return res