def solution(price, money, count):
    sum = 0
    for i in range(1, count+1):
        sum += price * i
    
    if sum-money > 0:
        return sum-money
    else:
        return 0
    
def solution(price, money, count):
    result = sum([i*price for i in range(1, count +1)]) - money  
    if result > 0:
        return result
    else:
        return 0

def solution(price, money, count):
    return sum([i*price for i in range(1, count +1)]) - money if sum([i*price for i in range(1, count +1)]) - money > 0 else 0


def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money) # 뒤에 값이 마이너스 값이 나오면 0이 최대값이 된다.


a = solution(1, 20,4)
print(a)