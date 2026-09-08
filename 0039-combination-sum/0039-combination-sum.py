class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        n=len(candidates)
        res=[]
        diary=[]

        def fun(idx,sum):
            if idx==n:
                if sum==target:
                    res.append(diary.copy())
                return res

            #choice 1: nhi lena hain element
            fun(idx+1,sum)

            #choice 2:lena hain element
            if sum+candidates[idx]<=target:
                diary.append(candidates[idx])
                sum+=candidates[idx]
                fun(idx,sum)  #yaha loop mein jaana hain kyunki element repeat kar sakte 
                diary.pop()
                sum-=candidates[idx]
        fun(0,0)
        return res

         


        