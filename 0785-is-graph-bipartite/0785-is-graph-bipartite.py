class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        colors=[-1 for _ in range(len(graph))]
        res=True
        def dfs(node,c):
            nonlocal res
            colors[node]=c
            for j in range (len(graph[node])):
                neigh=graph[node][j]
                if colors[neigh]!=-1 and colors[neigh]==c:
                    res=False
                if colors[neigh]==-1:
                    dfs(neigh,1-c)
        for k in range(len(graph)):
            if colors[k]==-1:
                dfs(k,0)
        return res

        