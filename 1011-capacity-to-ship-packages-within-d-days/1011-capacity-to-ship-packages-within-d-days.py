class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        res=0
        while low<=high:
            guess=(low+high)//2
            current_weight=0
            current_day=1
            for w in weights:
                if current_weight+w>guess:
                    current_day+=1
                    current_weight=w
                else:
                    current_weight+=w
            if current_day<=days:
                res=guess
                high=guess-1
            else:
                low=guess+1
        return res