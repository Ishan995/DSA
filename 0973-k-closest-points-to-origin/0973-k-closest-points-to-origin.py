import heapq
from typing import List


# Pair class with explicit else block for tie handling
class Pair:

  def __init__(self, dist: float, point: List[int]):
    self.first = dist  # distance squared
    self.second = point  # [x, y] coordinates

  def __lt__(self, other: "Pair") -> bool:
    # 1. Compare distances (Max-Heap behavior)
    if self.first != other.first:
      return self.first > other.first
    else:
      # 2. Equal distances: order doesn't matter for LC 973,
      # so return False to preserve insertion order cleanly.
      return False


class Solution:

  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    pq = []

    for x, y in points:
      # Squared distance to avoid sqrt calculation
      dist = x * x + y * y
      curr = Pair(dist, [x, y])

      if len(pq) < k:
        heapq.heappush(pq, curr)
      else:
        # Pushes curr, then pops the point with the largest distance
        heapq.heappushpop(pq, curr)

    # Extract elements using your p.second syntax
    res = []
    while pq:
      p = heapq.heappop(pq)
      res.append(p.second)

    return res
        

        
    

        
        