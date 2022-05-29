from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        node=defaultdict(int)
        left=set(edges[0])
        # 중심센터는 결국 n-1개의 degree를 가짐
        for edge in edges:
            left=left&set(edge)
        return list(left)[0]