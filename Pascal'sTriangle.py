class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal=[[1]]
        num=1
        while num<numRows:
            num+=1
            x=[1]*(num)
            pascal.append(x)
            # ģ ķģ A(k,m)=A(k-1,m-1)+A(k-1,m)
            #kė level
            for m in range(1,num-1):
                pascal[num-1][m]=pascal[num-2][m-1]+pascal[num-2][m]
        return pascal
                