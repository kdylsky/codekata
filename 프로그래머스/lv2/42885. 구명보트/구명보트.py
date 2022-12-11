"""
문제풀이
1.사람들을 오름차순으로 정렬한다. 
2.몇번을 반복할 지 모르니까 while을 사용한다.
3.첫번째와 맨 마직막을 더했을 때 값이 limit보다 작다면 둘다 제거하고 cnt+=1
4.그렇지 않다면 맨마지막에서 하나를 빼주고 cnt+=1
5.people의 길이가 1이 된다면 return
"""

from collections import deque

def solution(people, limit):
    deque_lst =deque(sorted(people)) 
    cnt = 0
    while True:
        if len(deque_lst) == 1 or len(deque_lst)==0:
            return cnt+1 if len(deque_lst)==1 else cnt
        elif deque_lst[0] + deque_lst[-1] <= limit:
            deque_lst.popleft()
            deque_lst.pop()
        else:
            deque_lst.pop()   
        cnt+=1