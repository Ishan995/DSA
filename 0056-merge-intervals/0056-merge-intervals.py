class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[]
        for i in range (len(intervals)):
            s2=intervals[i][0]
            e2=intervals[i][1]
            if len(res)==0:
                res.append([s2,e2])
            else:
                last=len(res)-1
                s1=res[last][0]
                e1=res[last][1]

                if e1>=s2:
                    res[last][1]=max(e1,e2)
                else:
                    res.append([s2,e2])

        return res

        

        