class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer=[]
        n=len(graph)
        stack=[(0,[0])]
        #possible path list
        while stack:
            node,path=stack.pop()
            #if node's edge exist
            if node==n-1:
                answer.append(path)
                continue
            else:
                for k in graph[node]:
                    stack.append((k,path+[k]))
                