height = [4,2,0,3,2,5]


left, right = 0, len(height)-1

l_max, r_max = height[left], height[right]

answer = 0
while left <= right:
    l_max = max(height[left],l_max)
    r_max = max(height[right],r_max)

    if l_max <= r_max :
        answer += l_max - height[left]
        left += 1
    else :
        answer += r_max - height[right]
        right -= 1
print(answer)