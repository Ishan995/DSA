class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        res={}

        for i in range(len(nums2)-1,-1,-1):
            num=nums2[i]
            while st and st[-1]<=num:
                st.pop()
            res[num]=st[-1] if st else -1
            st.append(num)
        return [res[x] for x in nums1]

        
            

        