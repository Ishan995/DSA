class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1=len(s1)
        len2=len(s2)

        if len1>len2:
            return False
        
        s1_count=Counter(s1)
        s2_count=Counter(s2[0:len1])

        if s1_count==s2_count:
            return True
        
        for i in range(len1,len2):
            right_char=s2[i]
            s2_count[right_char]+=1
            left_char=s2[i-len1]
            s2_count[left_char]-=1

            if s2_count[left_char]==0:
                del s2_count[left_char]

            if s1_count==s2_count:
                return True
        return False



        