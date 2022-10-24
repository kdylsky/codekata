def solution(d, budget):
    sum = 0
    
    for k, i in enumerate(sorted(d),1):
        sum += i
        if budget < sum:
            return k-1
    else:
        return k

d= [2,5,2,3,3,1,]
budget=10
a = solution(d, budget)
print(a)