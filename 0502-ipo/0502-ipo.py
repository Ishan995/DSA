class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        n=len(profits)
        proj=[]
        for i in range(n):
            proj.append((capital[i],profits[i]))
        proj.sort()

        idx=0
        max_pq=[]

        for i in range(k):
            while idx<n:
                if proj[idx][0]>w:
                    break
                else:
                    heapq.heappush(max_pq,-proj[idx][1])
                    idx+=1
            if not max_pq:
                return w
            else:
                w+= -heapq.heappop(max_pq)
        return w

        