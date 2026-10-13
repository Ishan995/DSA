from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float('inf')
        curr_sum = 0
        q = deque()
        
        for i in range(len(nums)):
            curr_sum += nums[i]  # FIX: Use += to build the running prefix sum

            # Base case: if the prefix sum from index 0 is >= k
            if curr_sum >= k:
                res = min(res, i + 1)

            # Shrink window from the left if valid
            while q and curr_sum - q[0][0] >= k:
                prefix_sum, idx = q.popleft()
                res = min(res, i - idx)

            # Maintain monotonic increasing order in the queue
            while q and curr_sum <= q[-1][0]:
                q.pop()

            q.append((curr_sum, i))

        return res if res != float('inf') else -1




        