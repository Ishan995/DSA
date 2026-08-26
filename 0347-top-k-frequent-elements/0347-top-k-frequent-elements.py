import heapq
from collections import Counter
from typing import List

# Pair class matching your handwritten syntax
class Pair:
    def __init__(self, first: int, second: int):
        self.first = first    # frequency
        self.second = second  # number element

    def __lt__(self, other: "Pair") -> bool:
        # Min-heap comparison based on frequency
        if self.first != other.first:
            return self.first < other.first
        else:
            # For LC 347, tie-breaking order doesn't matter,
            # so standard comparison works perfectly.
            return self.second < other.second


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each element
        freq_map = Counter(nums)

        # Step 2: Min-heap using your Pair object
        pq = []

        for element, freq in freq_map.items():
            curr = Pair(freq, element)

            if len(pq) < k:
                heapq.heappush(pq, curr)
            else:
                # Push curr first, then pop top element (smallest priority)
                heapq.heappushpop(pq, curr)

        # Step 3: Extract elements using your p.second syntax
        res = []
        while pq:
            p = heapq.heappop(pq)
            res.append(p.second)

        return res