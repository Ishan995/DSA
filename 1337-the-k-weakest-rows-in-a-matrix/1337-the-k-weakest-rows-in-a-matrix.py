class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        def countOnes(row):
            low=0
            high=len(row)-1
            while low<=high:
                mid=(low+high)//2
                if row[mid]==1:
                    low=mid+1
                else:
                    high=mid-1
            return low #will return no.of ones

        row_strength=[]
        for i,row in enumerate(mat):
            soldier_count=countOnes(row)
            row_strength.append((soldier_count,i))
        row_strength.sort()

        top_k_rows=row_strength[0:k]
        res=[]
        for count_of_soldiers,row_index in top_k_rows:
            res.append(row_index)
        return res



        