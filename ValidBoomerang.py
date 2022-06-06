class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # 기울기 문제
        x1,y1=points[0][0],points[0][1]
        x2,y2=points[1][0],points[1][1]
        x3,y3=points[2][0],points[2][1]
        s=set()
        for point in points:
            s.add(tuple(point))
        if len(points)-len(s)>=1:
            return False
        # in same line
        if x1==x2 and x1==x3:
            return False
        if x1!=x2 and x1!=x3:
            return (y1-y2)/(x1-x2)!=(y1-y3)/(x1-x3)
        return True