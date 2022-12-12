def solution(n,a,b):
    lst = list(range(1, n+1))
    cnt = 0
    while True:
        k = [(lst[x-1],lst[x]) for x in range(1, len(lst)+1, 2)]
        lst = []
        for i in k:
            if a not in i and b not in i:
                lst.append(i[0])
            elif a in i and b in i:
                return cnt+1
            elif a in i and b not in i:
                lst.append(a)
            elif b in i and a not in i:
                lst.append(b)
        cnt+=1
