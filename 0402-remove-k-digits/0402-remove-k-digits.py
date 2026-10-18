class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k>=len(num):
            return"0"
        st=[]
        for digit in num:
            while k>0 and st and st[-1]>digit:
                k-=1
                st.pop()
            st.append(digit)
        #case if num=1234,If we still have deletions left, slice them off the end
        if k>0:
            st=st[0:-k]
        res="".join(st).lstrip("0")
        return res if res else "0"
    
        
       

            

        
        



        