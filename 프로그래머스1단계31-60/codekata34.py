# 풀이1
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

# 풀이2 리스트컴프리헨션
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]

# 풀이3 map과 lambda
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

    
array =	[1, 5, 2, 6, 3, 7, 4]
commands =[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
result = solution(array, commands)
print(result)