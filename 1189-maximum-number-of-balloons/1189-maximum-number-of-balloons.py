class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        have={}
        for c in text:
            have[c]=have.get(c,0)+1
        
        need={"b":1,"a":1,"l":2,"o":2,"n":1}

        res=float('inf')

        for c,fneed in need.items():
            fhave=have.get(c,0)
            times=fhave//fneed
            res=min(res,times)

        return res


        
