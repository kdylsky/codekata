"""
문제풀이

1.n을 2진수로 변환하고 1의 갯수를 변수에 저장한다.
2.몇 번 반복할지 모르니까 while을 사용한다.
3.n+1의 2진수 변환 후 1의 개수를 확인한다.
4.0의 갯수가 같다면 break 후 return n+1 
"""

def solution(n):
    n_cnt = format(n, "b").count("1")
    while True:
        n_plus_cnt = format(n+1,"b").count("1")
        if n_plus_cnt == n_cnt:
            return n+1
        n=n+1