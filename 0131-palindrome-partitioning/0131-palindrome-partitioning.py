class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        diary=[]
        n=len(s)

        def fun(idx):
            if idx==n:
                res.append(diary.copy())
                return res
            
            for j in range(idx,n):
                sub=s[idx:j+1]  #idx:j+1 for slicing the string to get substring, also j+1 because yopu want the char at index j too, agar sirf j likhte toh sirf j se pehle tak ke char aate 
                if sub==sub[::-1]:
                    diary.append(sub)
                    fun(j+1)  # yahape j+1 kyunki next char pe jaake check karna hain palindrome
                    diary.pop()
        fun(0)
        return res




