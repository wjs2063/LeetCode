class Solution:
    def isThree(self, n: int) -> bool:
        # only three positive divisor menas that prime number**2 
        # 1<=n<=10^4 -> 1<=root(n)<=10^2
        prime={2}
        for i in range(3,100+1):
            prime.add(i)
            for j in range(2,int(i**0.5)+2):
                if i%j==0:
                    prime-={i}
                    break
        return n**0.5 in prime