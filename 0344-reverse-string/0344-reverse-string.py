class Solution:
    def reverseString(self, s: List[str]) -> None:
        st=[]
        n=len(s)

        for i in range(n):
            st.append(s[i])
        
        for i in range(n):
            c = st.pop()  
            s[i] = c  
            


       

        