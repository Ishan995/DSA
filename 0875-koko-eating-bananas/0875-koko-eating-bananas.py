class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high = max(piles)
        res=high 

        # eating speed = 1 2 3 4 5 6 7 8 9 10 11

        while low<=high:
            k=(low+high)//2
            hrs=0
            for p in piles:
                hrs+=math.ceil(p/k)
                
            if hrs>h:
                low=k+1
            else:
                res=min(res,k)
                high = k-1 #first occurence dhundna hain 

        return res




