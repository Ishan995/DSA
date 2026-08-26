from collections import Counter
import heapq
from typing import List


# Exact Pair class matching your handwritten structure
class Pair:

  def __init__(self, first: int, second: str):
    self.first = first  # frequency
    self.second = second  # word string

  def __lt__(self, other: "Pair") -> bool:
    # 1. Compare frequencies (Min-Heap behavior)
    if self.first != other.first:
      return self.first < other.first
    else:
      # 2. Tie-breaker for LC 692:
      # Use '>' so alphabetically larger words get popped/evicted first
      return self.second > other.second


class Solution:

  def topKFrequent(self, words: List[str], k: int) -> List[str]:
    # Step 1: Count frequencies
    freq_map = Counter(words)

    # Step 2: Min-heap using your Pair object
    pq = []

    for word, freq in freq_map.items():
      curr = Pair(freq, word)

      if len(pq) < k:
        heapq.heappush(pq, curr)
      else:
        # Pushes curr first, then pops the root (smallest priority)
        heapq.heappushpop(pq, curr)

    # Step 3: Extract elements matching your handwritten access syntax: (p.first, p.second)
    res = []
    while pq:
      p = heapq.heappop(pq)
      res.append(p.second)

    # Reverse because Min-Heap pops smallest frequencies first
    return res[::-1]