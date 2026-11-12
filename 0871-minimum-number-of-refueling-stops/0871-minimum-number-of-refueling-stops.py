class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        max_heap=[]
        prev_pos=0
        stops=0

        stations.append([target,0])

        for pos,fuel in stations:
            distance=pos-prev_pos
            startFuel-=distance

            while startFuel<0 and max_heap:
                startFuel+= -heapq.heappop(max_heap)
                stops+=1
            
            if startFuel<0:
                return -1

            heapq.heappush(max_heap,-fuel)
            prev_pos=pos

        return stops