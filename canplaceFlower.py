class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # ex) 10001 k=1 possible
        # 001001  k=1 possible k=2 impossible
        # left right side [0] append
        # sliding [0,0,0]
        flowerbed=[0]+flowerbed+[0]
        for i in range(len(flowerbed)-2):
            if flowerbed[i:i+3]==[0,0,0]:
                flowerbed[i+1]=1
                n-=1
        return n<=0