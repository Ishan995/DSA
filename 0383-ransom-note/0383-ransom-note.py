class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        f={}
        for c in magazine:
            f[c]=f.get(c,0)+1
        for c in ransomNote:
            if f.get(c,0)==0:
                return False
            else:
                f[c]-=1
        return True
          

        