class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        st=[n-1]
        res=[0]*n

        for i in range(n-2,-1,-1):
            while st and temp[st[-1]]<=temp[i]:
                st.pop()
            res[i]=st[-1]-i if st else 0
            st.append(i)
        return res

        