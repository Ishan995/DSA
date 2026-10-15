class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        res=[0]*n
        st=[]  #[temp,index]

        for i,t  in enumerate(temp):
            while st and t>st[-1][0]:
                st_temp,st_index=st.pop()
                res[st_index]=i-st_index
            st.append((t,i))
        return res   

        