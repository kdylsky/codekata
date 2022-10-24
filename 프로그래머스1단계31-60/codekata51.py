"""
콜라 문제 
"""

def solution(a, b, n):
    answer = 0
    while n >= a:
        new_cola = n // a * b 
        last_cola = n % a 
        n = new_cola+ last_cola
        answer += new_cola
    return answer


a = 2 # 한개의 콜라를 받기 위해서 반납하는 빈병의 개수	
b = 1 # 빈병을 a개 만큼 반납했을 때 받는 콜라의 개수
n = 20 # 가지고 있는 빈병이 개수
result = solution(a, b, n)
print(result)