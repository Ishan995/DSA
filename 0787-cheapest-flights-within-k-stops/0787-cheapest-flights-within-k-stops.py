class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        res=[float('inf')for _ in range(n)]
        res[src]=0
        
        for i in range(k+1):
            tmp=res.copy()
            for j in range(len(flights)):
                s=flights[j][0]
                d=flights[j][1]
                wt=flights[j][2]
                if res[s]!=float('inf') and res[s]+wt<tmp[d]:
                    tmp[d]=res[s]+wt
            res=tmp
        if res[dst]==float('inf'):
            return -1
        return res[dst]

                





        