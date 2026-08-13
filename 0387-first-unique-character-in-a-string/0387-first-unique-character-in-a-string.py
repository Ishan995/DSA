class Solution:
    def firstUniqChar(self, s: str) -> int:
        f={}

        for char in s:
            f[char]=f.get(char,0)+1

        for i in range(len(s)):
            if f[s[i]]==1:
                return i

        return -1
        