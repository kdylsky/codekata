def solution(left, right):
    sum = 0
    for i in range(left, right+1):
        if len([j for j in range(1, i+1) if i % j == 0]) % 2 == 0:
            sum += i
        else:
            sum -= i
    return sum

a =solution(24,27)
print(a)