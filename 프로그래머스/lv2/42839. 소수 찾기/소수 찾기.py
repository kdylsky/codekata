from itertools import permutations
def make_lst(numbers):
    numbers = list(numbers)
    temp = []
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            temp.append(int("".join(j)))

    return set(temp)

def primes(number):
    if number <2:
        return False
    for x in range(2, int(number**1/2)+1):
        if number%x ==0:
            return False
    return True


def solution(numbers):
    temp = make_lst(numbers)
    cnt = 0
    for i in temp:
        if primes(i):
            cnt+=1
    return cnt