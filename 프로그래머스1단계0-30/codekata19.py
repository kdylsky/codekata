def solution(n):
    answer = 0
    while answer <= n:
        answer += 1
        if n % answer == 1:
            return answer 

def solution(n):
    answer = [i for i in range(1, n+1) if n % i == 1][0]
    return answer

def solution(n):
    answer = 0
    while answer <= n:
        answer += 1
        if n % answer == 1:
            return answer 