class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        len_p=len(p)
        len_s=len(s)
        res=[]

        if len_p>len_s:
            return []
        
        p_count=Counter(p)
        s_count=Counter(s[0:len_p])

        if p_count==s_count:
            res.append(0)

        for i in range(len_p,len_s):
            right_char=s[i]
            s_count[right_char]+=1
            left_char=s[i-len_p]
            s_count[left_char]-=1

            if  s_count[left_char]==0:
                del  s_count[left_char]
            
            if s_count==p_count:
                res.append(i-len(p)+1)
            
        return res

        

