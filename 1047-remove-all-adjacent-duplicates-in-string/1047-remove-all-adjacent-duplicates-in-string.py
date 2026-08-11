class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]

    
        for char in s:
            if st and st[-1]==char:
                st.pop()
            else:
                st.append(char)
        
        return "".join(st)