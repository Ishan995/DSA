class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res=[]
        for i in range(len(intervals)):
            #no overlapping

            #agar interval sabse pehle hain append karna ho
            if (newInterval[1]<intervals[i][0]):
                res.append(newInterval)
                return res+intervals[i:]
                #interval ko end mein insert karna ho
            elif (newInterval[0]>intervals[i][1]):
                res.append(intervals[i])
            #overlapping
            else:
                newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]

        res.append(newInterval)
        return res


        