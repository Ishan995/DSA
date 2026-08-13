class Solution:
    def longestPalindrome(self, s: str) -> int:
        f={}
        for c in s:
            f[c]=f.get(c,0)+1
        
        res=0
        odd=False


        for c,val in f.items():
            if val%2==0:
                res+=val
            else:
                res+=val-1
                odd=True
         
        if odd:
            return res+1
        else:
            return res
    
           
        
        