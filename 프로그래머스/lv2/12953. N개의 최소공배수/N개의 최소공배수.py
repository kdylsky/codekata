import math

def lcm(a,b):
    return a*b//math.gcd(a,b)

def solution(arr):
    result = 1
    for i in arr:
        result = lcm(result, i)
    return result 