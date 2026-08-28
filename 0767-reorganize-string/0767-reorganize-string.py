class Solution:
    def reorganizeString(self, s: str) -> str:
        #hashmap to store count of characters
        count=Counter(s)
        #max heap
        pq=[[-freq,char]for char,freq in count.items()]
        heapq.heapify(pq)

        prev=None
        res=""
        
        while pq or prev:
            if prev and not pq:
                return ""
            else:    #Most freq char ko res mein daalo
                freq,char=heapq.heappop(pq)
                res+=char
                freq+=1  #+1 kyuki negative valu in max heap
            #prev ko heap mein push karo    
            if prev:
                heapq.heappush(pq,prev)
                prev=None #push karne ke baad abhi kuch nhi bacha prev mein
            if freq !=0:
                prev=[freq,char]
        return res


            




        