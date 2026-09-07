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

            #step 1:identify stages and step 2:idx
            
            if idx==n:
                res.append("".join(diary))
                return res
            
            #step3: choice?
            choice=digitToChar[s[idx]]

            #loop for all choices
            for j in range (len(choice)):
                #step 4
                diary.append(choice[j])
                fun(s,n,idx+1,diary,res)
                diary.pop()

            return res
        #step 5
        fun(digits,len(digits),0,diary,res)
        return res
        
        
            
     

       

        