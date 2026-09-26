class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        a=[[]for _ in range(n+1)]
        for edge in times:
            s=edge[0]
            d=edge[1]
            w=edge[2]
            a[s].append((d,w))
        dist=[float('inf') for _ in range(n+1)]
        dist[k]=0
        pq=[]
        heapq.heappush(pq,(0,k))
        while pq:
            dist_so_far,node=heapq.heappop(pq)
            if dist_so_far>dist[node]:
                continue
            for j in range(len(a[node])):
                neigh=a[node][j][0]
                wt=a[node][j][1]
                if dist_so_far+wt<dist[neigh]:
                    dist[neigh]=dist_so_far+wt
                    heapq.heappush(pq,(dist[neigh],neigh))
        max_time=max(dist[1:])
        if max_time==float('inf'):
            return -1
        else:
            return max_time



        