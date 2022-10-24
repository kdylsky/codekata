"""
실패율
실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
N = 전체 스테이지의 개수

stages = 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호
len(stages) = 게임에 참여하는 사람의 수

N+1 = 마지막까지 게임을 완료한 플레이어

스테이지에 도달한 유저가 없으면 0
실패율이 같다면 작은번호가 먼저오도록한다.

"""

def solution(N, stages):
    answer = []
    players = len(stages)
    temp = {}
    for i in range(1, N+1):
        cnt = 0
        for stage in stages:
            if i == stage:
                cnt+=1
        
        if cnt:
            temp[i] = cnt/players   
        else:
            temp[i] = 0
        players = players - cnt

    a = sorted(temp.items(), key=lambda x : x[1] ,reverse= True)
    for i in a:
        answer.append(i[0])
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
result = solution(N, stages)
print(result)
