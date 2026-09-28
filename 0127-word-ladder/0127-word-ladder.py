class Solution:
    def ladderLength(self, beginword: str, endword: str, wordList: list[str]) -> int:
        n=len(wordList)
        f=set(wordList)
        if endword not in f:
            return 0
        if beginword not in f:
            f.add(beginword)

        q=deque()
        q.append((beginword,1))
        if beginword in f:
            f.remove(beginword)  # to mark as visited such that word isnt repeated

        while q:
            p=q.popleft()
            s=p[0]
            val=p[1]
            if s==endword:
                return val
            for i in range(len(s)):
                c=s[i]
                for j in range(97,123):
                    ch=chr(j)
                    if c==ch:
                        continue
                    new_s = s[:i]+ch+s[i+1:]
                    if new_s in f:
                        q.append((new_s,val+1))
                        f.remove(new_s) 
        
        return 0
                    
        
        