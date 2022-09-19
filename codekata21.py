def solution(numbers):
    sum = 0
    for i in range(10):
        if i not in numbers:
            sum += i
    return sum

def solution(numbers):
    return sum(set([i for i in range(10)]) - set(numbers)) 

def solution(numbers):
    return 45 - sum(numbers)

    
numbers = [1,2,3,4,6,7,8,0]

result = solution(numbers)
print(result)


print(sum((["hu"],["hello"]),[]))