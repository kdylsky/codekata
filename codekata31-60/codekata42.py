# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    return [i* x for i in range(1,n+1)]
x = -4
n = 2
solution(x, n)


# 행렬의 덧셈
def solution(arr1, arr2):
    answer = []
    for k in range(len(arr1)):
        temp = []
        for i,j in zip(arr1,arr2):
            temp.append(i[k]+j[k])
        answer.append(temp)

    return answer
	
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
result = solution(arr1, arr2)


# 핸드폰 번호 가리기
def solution(phone_number):
    answer = ''
    cnt = len(phone_number)
    for i in phone_number:
        if cnt > 4:
            answer += "*"
            cnt -= 1
        else:
            answer += i
    return answer


def solution(phone_number):
    return (len(phone_number)-4) * "*" + phone_number[-4:]
    
phone_number ="121234888"
solution(phone_number)