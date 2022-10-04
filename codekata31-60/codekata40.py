def solution(n, lost, reserve): 
    new_lost = list(set(lost)- set(reserve))
    new_reserve = list(set(reserve)- set(lost))
    cnt = n - len(new_lost)
    
    for i in new_lost:
        if i-1 in new_reserve:
            cnt+=1
            new_reserve.remove(i-1)    
        elif i+1 in new_reserve:
            cnt+=1
            new_reserve.remove(i+1)

    return cnt

n = 3
reserve = [1,2,3]
lost = [1,2,3]

result = solution(n, lost, reserve)
print(result)