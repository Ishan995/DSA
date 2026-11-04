class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        if sum(candies)<k:
            return 0

        res=0
        low=1
        high=sum(candies)//k
        while low<=high:
            guess=(low+high)//2
            count=0
            for c in candies:
                if c>=guess:
                    count+=c//guess
                if count>=k:
                    break     #no need to search further
            if count>=k:
                res=guess
                low=guess+1
            else:
                high=guess-1
        return res
                    