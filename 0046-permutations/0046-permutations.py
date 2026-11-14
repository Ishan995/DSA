class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res=[]
        diary=[]
        n=len(nums)

        def fun():
            if len(diary)==n:
                res.append(diary.copy())
                return 
            
            for j in range(n):
                if nums[j] in diary:
                    continue
                diary.append(nums[j])
                fun()
                diary.pop()

        fun()
        return res
        