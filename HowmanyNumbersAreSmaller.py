class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s=sorted(nums)
        indexing=dict()
        for i in range(len(s)):
            # sorting 된 list 의 index 를 저장
            if s[i] not in indexing:
                indexing[s[i]]=i
        answer=[]
        for i in range(len(nums)):
            answer.append(indexing[nums[i]])
        return answer