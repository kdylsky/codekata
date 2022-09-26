def solution(n, lost, reserve):
    answer = 0
    std_list = [i for i in range(1, n+1)]
    temp = list(set(lost).intersection(reserve))
    if temp:
        lost = list(set(lost) - set(temp))
        reserve = list(set(reserve) - set(temp))

    cnt = len(list(set(std_list)- set(lost)))
    
    test = {}
    for i in lost:
        if i == 1:
            test[i] = i+1
        elif i == n:
            test[i] = i-1
        else:
            test[i] = i-1, i+1

    print(test)
   

    
    
    # for i in lost:
    #     if i == 1:
    #         if i+1 in reserve:
    #             cnt += 1
    #             reserve.remove(i+1)
                
    #     elif i == n:
    #         if i-1 in reserve:
    #             cnt += 1
    #             reserve.remove(i-1)
        
    #     elif i-1 or i+1 in reserve:
    #         if i-1 and i+1:
    #             cnt +=1
    #             reserve.remove(i-1)
    #         elif i-1 and not i+1:
    #             cnt +=1
    #             reserve.remove(i-1)
    #         elif not i-1 and i+1:
    #             cnt +=1
    #             reserve.remove(i+1)
    return cnt



