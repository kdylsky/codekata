"""
문제풀이
1. 몇번 반복할 지 모르기 때문에 while을 쓴다.
2. s = "1"일 될 때 까지 반복한다.
3. 몇번 반복했는지 알기 위한 cnt, 몇 개의 0이 사라진지 알기 위한 sum
4. 맨처음 돌때 s의 0의 갯수를 구한다.
5. s의 원래길이에서 0의 갯수를 뺀 수를 다시 2진법으로 바꾸고 s에 대입한다.
"""

def solution(s):
    cnt = 0 
    sum = 0
    while s != "1":
        s_cnt = len(s)
        zero_cnt = s.count("0")
        s = format(s_cnt - zero_cnt, "b")
        sum += zero_cnt
        cnt +=1
    return [cnt, sum] 