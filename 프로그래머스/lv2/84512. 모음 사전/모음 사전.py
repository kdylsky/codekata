from itertools import product
def solution(word):
    temp = []
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(1,6):
        for per in product(alpha,repeat = i):
            temp.append(''.join(per))
    print(temp)
    temp.sort()
    return temp.index(word)+1