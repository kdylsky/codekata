"""
최대공약수와 최소공배수

두수의 최대공약수는 내장함수 math의 gcd()를 이용하면 간단히 구할 수 있다.
두 자연수의 곱 = 최대공약수 * 최소공배수
최소공배수 = 두자연수의곱 // 최대공약수

"""

import math
def solution(n, m):
    answer = []
    temp  = math.gcd(n,m)
    temp2 = (n*m) // temp     
    answer.append(temp)
    answer.append(temp2)
    return answer

def solution(n, m):
    answer = []
    a = [i for i in range(1, m+1) if m%i == 0]
    b = [i for i in range(1, n+1) if m%i == 0]
    c = max(list(set(a).intersection(set(b))))
    d = (n*m) // c
    answer.append(c)
    answer.append(d)

    return answer

n = 3
m = 12
result = solution(n, m)



