class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_del=arr[0]
        one_del=-1
        res=arr[0]

        for i in range(1,len(arr)):
            prev_nodel=no_del
            no_del=max(prev_nodel+arr[i],arr[i])
            one_del=max(one_del+arr[i],prev_nodel)
            res=max(res,one_del,no_del)

        return res




        