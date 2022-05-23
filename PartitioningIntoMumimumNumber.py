n = "27346209830709182346"
# 각 자리수의 합은 Independent 하기때문에 자리수의max를구하면됨
n=list(map(int,list(n)))
print(max(n))