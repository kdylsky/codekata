def solution(citations):
    temp = []
    for i in range(1, len(citations)+1):
        a = len([t for t in citations if t >= i])
        print(i, a)
        if i <= a:
            temp.append(i)
    
    return max(temp) if temp else 0