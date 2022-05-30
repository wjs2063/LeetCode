from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        def dfs():
            s=source
            d=destination
            stack=[s]
            visited=[False]*n
            while stack:
                x=stack.pop()
                if x==d:
                    return True
                if not visited[x]:
                    visited[x]=True
                    for e in graph[x]:
                        stack.append(e)
            return False
        return dfs()
                        