"""
문제풀이
1. 두개를 더한 값의 약수의 집합을 temp에 담는다.
2. temp를 돌면서 (x-2)*(y-2) = yellow 에 해당하는 값만을 따로 result에 담는다.
"""

def solution(brown, yellow):
    sum = brown + yellow
    temp = []
    for i in range(1,sum//2+1):     
        if sum%i == 0:
            temp.append((i, sum//i))
    result = []
    for i in temp:
        if (i[0]-2)*(i[1]-2) == yellow:
            result.append(i)
    return result[-1]