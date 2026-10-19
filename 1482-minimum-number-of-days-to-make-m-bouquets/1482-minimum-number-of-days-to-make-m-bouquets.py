class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        def canMake(days):
            flowers=0
            bouqets=0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=days:
                    flowers+=1
                    if flowers==k:
                        bouqets+=1
                        flowers=0
                else:
                    flowers=0
            if bouqets>=m:
                return True 
            else:
                return False
        
        low=min(bloomDay)
        high=max(bloomDay)
        ans=-1
        while low<=high:
            guess=(low+high)//2
            if canMake(guess):
                ans=guess
                high=guess-1
            else:
                low=guess+1
        return ans
                



                    



        