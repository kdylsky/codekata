
def make_set(str):
    temp = []
    for i in range(1, len(str)): 
        if ord(str[i-1]) in (range(97,123)) and ord(str[i]) in (range(97,123)):
            word = str[i-1]+str[i]
            temp.append(word)
    return temp

def count_intersection(str1, str2):
    inter = []
    temp_str2 = str2.copy()
    for i in str1:
        if i in temp_str2:
            temp_str2.remove(i)
            inter.append(i)
    return len(inter)

def count_union(str1, str2):
    union_one = str1.copy()
    union_two = str1.copy()
    for x in str2:
        if x not in union_one:
            union_two.append(x)
        else:
            union_one.remove(x)

    return len(union_two)

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()   
    str1 = make_set(str1)
    str2 = make_set(str2)
    inter = count_intersection(str1, str2)
    union = count_union(str1, str2)
    answer = 0
    if inter and union:
        answer=int(inter/union*65536)
    elif not inter and union:
        answer=0        
    elif not inter and not union:
        answer=1*65536
    return answer