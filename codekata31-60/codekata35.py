def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    new_a = a * int(10000/len(a))
    new_b = b * int(10000/len(b))
    new_c = c * int(10000/len(c))

    idx = 0

    result = {1:0, 2:0, 3:0}
    
    for i in answers:
        if i == new_a[idx]:
            result[1] += 1
        if i == new_b[idx]:
            result[2] += 1
        if i == new_c[idx]:
            result[3] += 1

        idx += 1
    
    answer = []
    for key in result.keys():
        if result[key] == max(list(result.values())):
            answer.append(key)
  
    return answer
answer = [1,2,3,4,5]
a = solution(answer)
# print(a)






