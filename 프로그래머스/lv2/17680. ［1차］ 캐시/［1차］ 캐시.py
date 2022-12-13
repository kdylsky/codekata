"""
문제풀이
1.deque를 이용한다.
2.초기세팅으로 cacheSize 만큼의 도시를 넣어주고, 해당 초들 계산해준다.
3.그 후 하나씩 돌면서 조건으로 들어있는지 확인하고 아니면 넣는다.
4.있다면 해당 deque안에 있는 모든 것을 빼서 다시 넣어준다. 그래야지 최신순이 다시 정렬된다.
"""

from collections import deque

def solution(cacheSize, cities):
    cities = list(map(lambda x : x.lower() , cities))
    deque_lst = deque(maxlen=cacheSize)
    answer=0
    for x in cities:
        if x not in deque_lst:
            answer+= 5
            deque_lst.append(x)
        else:          
            answer+=1
            for _ in range(len(deque_lst)):
                a = deque_lst.popleft()
                if a != x:
                    deque_lst.append(a)
            deque_lst.append(x)
    return answer
