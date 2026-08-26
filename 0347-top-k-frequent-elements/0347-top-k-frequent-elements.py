class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each element
        freq_map = Counter(nums)
        
        # Min-heap to store pairs of (freq, element)
        pq = []
        
        # Step 2: Iterate through frequency map (auto i : mp)
        for element, freq in freq_map.items():
            curr = (freq, element)
            
            # If heap size is less than k, push and continue
            if len(pq) < k:
                heapq.heappush(pq, curr)
                continue
            
            # Compare current frequency with top of min-heap
            if freq <= pq[0][0]:
                continue
            
            heapq.heappop(pq)
            heapq.heappush(pq, curr)
            
        # Step 3: Extract elements from the heap into result vector
        res = []
        while pq:
            res.append(heapq.heappop(pq)[1])
            
        return res