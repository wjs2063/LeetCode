from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group=defaultdict(list)
        answer=[]
        # group size별로 해당하는 person을 push
        for index,value in enumerate(groupSizes):
            group[value].append(index)
            # value 에 해당하는 list의 길이가 value가되면 answer에 push
            if len(group[value])==value:
                answer.append(group[value])
                group[value]=[]
        return answer
        