from collections import Counter
def solution(participant, completion):
    new_part = Counter(participant)
    new_comp = Counter(completion)
    print((new_part- new_comp).keys())
    for i,j in new_part.items():
        if abs(new_comp[i] - j) != 0:
            return i

def solution(participant, completion):
    new_part = Counter(participant)
    new_comp = Counter(completion)
    return list((new_part- new_comp).keys())[0]
    


def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
        
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    
    return answer

   

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
a = solution(participant, completion)
print(a)

