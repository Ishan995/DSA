class Solution:

  def nextGreaterElements(self, nums: List[int]) -> List[int]:
    n=len(nums)
    res=[-1]*n
    st=[]

    for i in range (n-1,-1,-1):
        st.append(i)

    for i in range(n-1,-1,-1):
        while st and nums[st[-1]]<=nums[i]:
            st.pop()
        res[i]=nums[st[-1]] if st else -1
        st.append(i)
    return res


        