"""
롤케이크 자르기
"""

def solution(topping):
    count = 0
    for i in range(len(topping)+1):
        if len(set(topping[:i])) == len(set(topping[i:])):
            count += 1
    return count

topping = [1, 2, 1, 3, 1, 4, 1, 2]
a = solution(topping)
print(a)


from collections import Counter

def solution(topping):
    dic = Counter(topping)
    set_dic = set()
    
    res = 0
    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            res += 1
    return res

topping = [1, 2, 1, 3, 1, 4, 1, 2]
a = solution(topping)
