class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st=[]  # [char,count]

        for c in s:
            if st and st[-1][0]==c:
                st[-1][1]+=1
            else:
                st.append([c,1])
            if st[-1][1]==k:
                st.pop()
        res=""
        for char, count in st:
            res+= (char*count)
        return res

        