class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum=[]
        val=0
        altitude=[0]
        for g in gain:
            val+=g
            altitude.append(val)
        return max(altitude)