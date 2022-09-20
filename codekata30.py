def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            temp = numbers[i]+ numbers[j]
            if temp in answer:
                continue
            answer.append(temp)
        answer.sort()
    return answer


from itertools import combinations
from itertools import permutations
from itertools import product
def solution(numbers):
    answer = []
    l = list(combinations(numbers, 3))
    for i in l:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()

    return answer

numbers = [2,1,3,4,1]
a = solution(numbers)


test = [1,2,3,4,5]
test2 = ["A","B"]
test3 = [[1,2,3,4,5],["a","b","c","d","e"]]
result = list(combinations(test,2))
# [(1, 2), (1, 3), (1, 4), (1, 5), 
# (2, 3), (2, 4), (2, 5), 
# (3, 4), (3, 5), 
# (4, 5)]

result = list(permutations(test,2))
# [(1, 2), (1, 3), (1, 4), (1, 5), 
# (2, 1), (2, 3), (2, 4), (2, 5), 
# (3, 1), (3, 2), (3, 4), (3, 5), 
# (4, 1), (4, 2), (4, 3), (4, 5), 
# (5, 1), (5, 2), (5, 3), (5, 4)]

result = list(product(test, test2))
#[(1, 'A'), (1, 'B'), 
# (2, 'A'), (2, 'B'), 
# (3, 'A'), (3, 'B'), 
# (4, 'A'), (4, 'B'), 
# (5, 'A'), (5, 'B')]

result = list(product(*test3))
#[(1, 'a'), (1, 'b'), (1, 'c'), (1, 'd'), (1, 'e'), 
# (2, 'a'), (2, 'b'), (2, 'c'), (2, 'd'), (2, 'e'), 
# (3, 'a'), (3, 'b'), (3, 'c'), (3, 'd'), (3, 'e'), 
# (4, 'a'), (4, 'b'), (4, 'c'), (4, 'd'), (4, 'e'), 
# (5, 'a'), (5, 'b'), (5, 'c'), (5, 'd'), (5, 'e')]

