from functools import reduce

def solution(clothes):
    dic = {}
    for value, key in clothes:
        if dic.get(key):
            dic[key] += [value]
        else:
            dic[key] = [value]
    a = [len(i)+1 for i in dic.values()]
    case = reduce(lambda x,y : x*y, a)
    return case -1
