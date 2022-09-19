def solution(priorities, location):
    lst = []
    final_lst = []
    
    for i in range(len(priorities)):
        lst.append((priorities[i],chr(i+65)))
  
    target = lst[location]
    
    while len(lst) != 0:
        max_num = max(lst)[0]

        if max_num == lst[0][0]:
            final_lst.append(lst[0])
            lst.pop(0)
        else:
            lst.append(lst.pop(0))    

    return final_lst.index(target) + 1  

priorities = [2, 1, 3, 2]
# priorities = [1,1,1,9, 1, 1]
location = 1


