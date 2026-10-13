class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        res=float('inf')
        curr_sum=0
        q=deque()
        for i in range (len(nums)):
            curr_sum+=nums[i]
            if curr_sum>=k:
                res=min(res,i+1)
            while q and curr_sum-q[0][0]>=k:
                prefix_sum,idx=q.popleft()
                res=min(res,i-idx)
            while q and curr_sum<=q[-1][0]:
                q.pop()
            q.append((curr_sum,i))

        return res if res!=float('inf') else -1




        