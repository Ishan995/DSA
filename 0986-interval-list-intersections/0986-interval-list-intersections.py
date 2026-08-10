class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        res=[]
        i=0
        j=0
        n=len(a)
        m=len(b)

        while i<n and j<m:
            s1=a[i][0]
            e1=a[i][1]
            s2=b[j][0]
            e2=b[j][1]
            if s1<=s2:
                if e1>=s2:
                    s=max(s1,s2)
                    e=min(e1,e2)
                    res.append([s,e])
            else :
                if e2>=s1:
                    s=max(s2,s1)
                    e=min(e2,e1)
                    res.append([s,e])
        
            if e1<=e2:
                i+=1
            else :
                j+=1

        return res
        


            

        