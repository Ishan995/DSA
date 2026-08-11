class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for char in s:
            if char=="("or char=="[" or char=="{":
                st.append(char)
            else:
                if len(st)==0:
                    return False
                top=st.pop()
                if char==")" and top!="(":
                    return False
                if char=="]" and top!="[":
                    return False
                if char=="}" and top!="{":
                    return False
        return len(st) == 0
       
        