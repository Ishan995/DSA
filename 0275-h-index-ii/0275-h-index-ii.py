class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n=len(citations)
        low=0
        high=n-1
        while low<=high:
            guess=(low+high)//2
            if citations[guess]==n-guess:
                return citations[guess]
            elif citations[guess]>n-guess:
                high=guess-1
            else:
                low=guess+1

        return n-low
        