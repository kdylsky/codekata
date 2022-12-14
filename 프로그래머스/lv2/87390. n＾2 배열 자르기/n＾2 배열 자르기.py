def solution(n, left, right):
    answer=[]

    for i in range(left//n,n):
        for j in range(n):
            if i*n+j >= left and i*n+j <= right:
                answer.append(max(i,j)+1)
            elif i*n+j > right:
                return answer

    return answer