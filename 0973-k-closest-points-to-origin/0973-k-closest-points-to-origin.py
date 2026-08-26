class Pair:
    def __init__(self,dist:float,point:List[int]):
        self.first=dist
        self.second=point
    def __lt__(self,other:Pair) ->bool:
        if self.first!=other.first:
            return self.first>other.first
    
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq=[]
        for x,y in points:
            dist=x*x + y*y
            curr=Pair(dist, [x,y])
            if len(pq)<k:
                heapq.heappush(pq,curr)
            else:
                heapq.heappushpop(pq,curr)
        res=[]
        while pq:
            p=heapq.heappop(pq)
            res.append(p.second)
        return res
        

        
    

        
        