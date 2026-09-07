class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res=[]
        diary=[]

        def fun(s,n,idx,diary,res):
            if idx==n:
                res.append("".join(diary))
                return res
            
            choice=digitToChar[s[idx]]

            for j in range (len(choice)):
                diary.append(choice[j])
                fun(s,n,idx+1,diary,res)
                diary.pop()

            return res
        
        fun(digits,len(digits),0,diary,res)
        return res
        
        
            
     

       

        