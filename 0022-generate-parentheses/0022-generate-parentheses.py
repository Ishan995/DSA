class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        tmp=[]
        res=[]

        def fun(open_count,close_count):
            
            #final condition
            if open_count==n and close_count==n:
                res.append("".join(tmp))
                return res
            
            #open append karna hain
            if open_count<n:
                tmp.append("(")
                fun(open_count+1,close_count)
                tmp.pop()
            
            #close append karna hain
            if close_count<open_count:
                tmp.append(")")
                fun(open_count,close_count+1)
                tmp.pop()

        fun(0,0)
        return res

                

            


        