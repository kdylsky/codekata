"""
짝수와 홀수
num이 주어질 경우 짝수인지 홀수인지를 분기를 통해서 판단
"""
def solution(num):
    return "Even" if num % 2 == 0 else "Odd"


"""
제일 작은 수 제거하기
배열이 주어질 경우 배열에서 제일 작은 수를 제거해서 반환하라.

제일 작은 수를 구하는 것은 min을 이용해서 구하면 된다.
만약 배열에 제일 작은수가 여러개인 경우라면 모두 제거한 것을 반환한다.

"""

def solution(arr):
    min_num = min(arr)
    result = [i for i in arr if i != min_num]

    if len(result) == 0:
        result.append(-1)
    return result


"""
정수 제곱근 판별

임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

math.sqrt(121) # 11.0 제곱근
math.pow(11,2) # 121.0 제곱


"""
def solution(n):
    temp = int(n**(1/2))
    if n == temp**2:
        return (temp+1)**2
    else:
        return -1


import math

def solution(n):
    temp = int(math.sqrt(n))
    if math.pow(temp,2) == n:
        return math.pow(temp+1, 2)
    else:
        return -1



"""
정수 내림차순으로 배치하기

함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

1.정수 n을 문자열로 바꾸어 준다.
2.sort()메서드를 이용해서 내림차순으로 만들어준다(reversed = True)
3.int로 변경 후 반환한다.

"""

def solution(n):
    answer = 0
    str_n = str(n)
    temp = sorted(str_n, reverse=True)
    
    return int("".join(temp))


"""
자연수 뒤집어 배열로 만들기

1.n을 리스트로 만든다.
2.reverse()를 이용해서 정렬해준다.

"""

def solution(n):
    n = list(str(n))
    n = list(map(int, n))
    n.reverse()    
    return n


"""
자릿수 더하기

1.숫자를 문자로 만든다.
2.원소가 정수인 리스트로 만든다.
3.sum()함수를 이용해서 return 한다.

"""

def solution(n):
    str_n = str(n)
    lst = map(int,list(str_n))
    temp = sum(lst)
    return temp



"""
이상한 문자 만들기

문제 설명
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

1. 먼저 문자를 공백을 기준으로 나누어서 리스트로 만든다.
2. 이중반복문을 사용한다.
2-1 첫번째 반복문에는 단어가 들어오게 한다.
2-2 두번째 반복문은 단어의 길이를 기준으로 돌게한다.

3. 두번째 반복문을 돌면서 인덱스를 이용해서 짝수/홀수를 구분해서 구해준다.


"""
def solution(s):
    answer = ''
    idx = 0
    for i in s:
        if i != " ":
            if idx %2 == 0:
                answer += i.upper()
                idx+= 1
            elif idx %2 != 0:
                answer += i.lower()
                idx+= 1
        else:
            answer += " "
            idx = 0
    return answer

s = "try hello world"

result = solution(s)
print(result)