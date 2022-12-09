"""
피보나치 수 만들기
0, 1, 1, 2, 3, 5, 8, 13, 21,...... 
"""

def solution(n):
    pibo = [0, 1]
    for i in range(n-1):
        pibo.append(pibo[-1]+pibo[-2])
    return pibo[-1]%1234567
