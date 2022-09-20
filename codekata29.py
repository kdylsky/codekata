def solution(n):
    temp = []
    while True:
        if n < 3 :
            temp.append(n)
            break
        
        temp.append(n%3)
        n = n//3    
    return sum([temp[i] * (3**j) for i, j in enumerate(range(len(temp)-1, -1, -1))])


def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer