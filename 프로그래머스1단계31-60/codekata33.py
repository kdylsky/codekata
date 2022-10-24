from curses import keyname


def solution(N, stages):
    answer = []
    people = len(stages)
    temp = [(i,stages.count(i)) for i in range(1, N+1)]
    print(temp)
    result = {}
    for i, j in temp:
        result[i] = j/people
        people -= j


    a = sorted(result.items(), key=lambda x: x[1], reverse=True)
    print(a)
    for i,j in a:
        answer.append(i)
    
    return answer

stages = [4,4,4,4,4]
N = 4

a = solution(N,stages)
# print(a)