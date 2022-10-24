from itertools import combinations
def is_prim(i):
    for k in range(2, i):
        if i%k == 0:
            return False
    return True

def solution(nums):
    result = list(combinations(nums,3))
    cnt = 0
    for i in result:
        if is_prim(sum(i)):
            cnt += 1
    return cnt

nums = [1,2,3,4]
result = solution(nums)
print(result)



def prime_number(x):
    answer = 0
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

result = prime_number(11)
print(result)


import math

n = 1000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화

# 에라토스테네스의 체 알고리즘 
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2 
        while i * j <= n:
            array[i * j] = False
            j += 1