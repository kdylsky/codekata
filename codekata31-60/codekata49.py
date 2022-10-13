"""
문자열 내 마음대로 정렬하기
문제 설명
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 
각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
예를 들어 strings가 ["sun", "bed", "car"]이고 
n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

첫번쨰 sorted를 해서 오름차순으로 만든다. n 인덱스에 해당하는 값이 같은 경우에 
사전순으로 먼저오는 알파벳으로 정렬하기 위함이다.

두번째 sorted에서는 정렬시 기준이 되는 값을 key 옵션을 이용해서 정해준다.
"""

def solution(strings, n):
    strings = sorted(strings)
    temp = sorted(strings, key= lambda x : x[n])
    
    return temp


"""
두 정수 사이의 합
문제 설명
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

1. a와 b중에서 큰값을 구한다.
2. range()를 이용해서 a와 b사이의 숫자 리스트를 만든다.
3. sum()함수를 이용해서 더해준다.

"""

def solution(a, b):
    max_num = max(a, b)
    min_num = min(a, b)
    return sum(range(min_num, max_num+1))

def solution(a, b):
    if a>b: 
        b,a = a,b
    return sum(range(a, b+1))


"""
나누어 떨어지는 숫자 배열
문제 설명
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

1. 리스트 컴프리헨션을 이용한 한줄 for문 만들기
2. 만약 리스트의 len() == 0이면 -1을 반환
3. 오름차순으로 만들기
"""

def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0 ]
    answer = sorted(answer)
    if len(answer) == 0:
        answer.append(-1)
    return answer
    
def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0 ]
    answer = sorted(answer)
    return answer if len(answer) != 0 else [-1]


"""
가운데 글자 가져오기
문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

1. 짝수인 경우와 홀수인 경우로 나눈다.
2. 홀수인 경우라면 len(s)//2로 몫을 구해서 몫==인덱스이므로 인덱스에 해당하는 문자열을 반환한다.
3. 짝수인 경우라면 len(s)//2로 몫을 구해서 몫-1, 몫 에 해당하는 문자열을 반환한다.

"""

def solution(s):
    answer = ''
    if len(s)%2 != 0:
        answer += s[len(s)//2]
    else:
        answer = s[(len(s)//2)-1 : len(s)//2 +1]
    return answer


"""
2016년
문제 설명
2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 
두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT입니다. 
예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

1,3,5,7,8,10,12 31일
4,6,9,11 30일
2 29일

1. 2016년 1월 1일은 금요일 days=1
2. 해당 월/일 까지의 전체 일수를 구한다.
3. 145일%7일
4. 값에 해당하는 요일의 인덱스를 반환한다.
"""



def solution(a, b):
    week = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    mon = {1:31, 2:29, 3:31, 4:30, 5:31,6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    days = b
    for i in range(1, a):
        days += mon[i]
    temp = days%7
    return week[temp-1]


import datetime
from re import X
from tkinter import Y
from typing import Counter
a = datetime.datetime(2016,5,29).weekday()

"""
폰켓몬
문제 설명
당신은 폰켓몬을 잡기 위한 오랜 여행 끝에, 홍 박사님의 연구실에 도착했습니다. 
홍 박사님은 당신에게 자신의 연구실에 있는 총 N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다고 했습니다.
홍 박사님 연구실의 폰켓몬은 종류에 따라 번호를 붙여 구분합니다. 
따라서 같은 종류의 폰켓몬은 같은 번호를 가지고 있습니다. 
예를 들어 연구실에 총 4마리의 폰켓몬이 있고, 각 폰켓몬의 종류 번호가 [3번, 1번, 2번, 3번]이라면 이는 3번 폰켓몬 두 마리, 
1번 폰켓몬 한 마리, 2번 폰켓몬 한 마리가 있음을 나타냅니다. 
이때, 4마리의 폰켓몬 중 2마리를 고르는 방법은 다음과 같이 6가지가 있습니다.

첫 번째(3번), 두 번째(1번) 폰켓몬을 선택
첫 번째(3번), 세 번째(2번) 폰켓몬을 선택
첫 번째(3번), 네 번째(3번) 폰켓몬을 선택
두 번째(1번), 세 번째(2번) 폰켓몬을 선택
두 번째(1번), 네 번째(3번) 폰켓몬을 선택
세 번째(2번), 네 번째(3번) 폰켓몬을 선택

이때, 첫 번째(3번) 폰켓몬과 네 번째(3번) 폰켓몬을 선택하는 방법은 한 종류(3번 폰켓몬 두 마리)의 폰켓몬만 가질 수 있지만,
다른 방법들은 모두 두 종류의 폰켓몬을 가질 수 있습니다. 따라서 위 예시에서 가질 수 있는 폰켓몬 종류 수의 최댓값은 2가 됩니다.
당신은 최대한 다양한 종류의 폰켓몬을 가지길 원하기 때문에, 최대한 많은 종류의 폰켓몬을 포함해서 N/2마리를 선택하려 합니다. 
N마리 폰켓몬의 종류 번호가 담긴 배열 nums가 매개변수로 주어질 때, 
N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 
그때의 폰켓몬 종류 번호의 개수를 return 하도록 solution 함수를 완성해주세요.

"""
def solution(nums):
    dit ={}
    for i in nums:
        dit[i] = i

    if len(dit) >= int(len(nums)/2):
        return int(len(nums)/2)
    else:
        return len(dit)
    

# 시간초과 발생
# 해시를 이용한 풀이이므로 O(1)상수시간 이내에 풀이가 가능해야한다.
from itertools import combinations
def solution(nums):
    a = combinations(nums, int(len(nums)/2))
    b = list(set(a))    
    result = []
    for i in b:
        result.append(len(set(i)))
    return max(result)



"""
숫자 짝꿍
문제 설명
두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 
정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다
(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). 
X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. 
X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

x와 y를 list와 set으로 만들어서 공통된 요소를 찾는다.
공통된 요소의 갯수를 센다.
갯수가 작은 것을 기준으로 새로운 리스트를 만든다.
내림차순으로 정렬한다.
문자열로 만든다.
"""

def solution(X, Y):
    answer = ''
    dit = {}
    temp = list(set(X).intersection(set(Y)))
    if len(temp) == 0:
        return "-1"
    if len(temp) == 1 and temp[0] == "0":
        return "0"
    for i in temp:
        x = X.count(i)
        y = Y.count(i)
        
        if x > y:
            dit[i] = y
        elif x <y:
            dit[i] = x
        else:
            dit[i] = x
    a = sorted(dit, key=lambda x : x[0] ,reverse= True)    
    for i in a:
        answer += i*dit[i]
    return answer


def solution(X, Y):
    from collections import Counter

    inter = Counter(X) & Counter(Y)
    if not inter:
        return "-1"
    elif "0" in inter and len(inter) == 1:
        return "0"
    return "".join(sorted(inter.elements())[::-1])



"""
삼총사
문제 설명
한국중학교에 다니는 학생들은 각자 정수 번호를 갖고 있습니다. 
이 학교 학생 3명의 정수 번호를 더했을 때 0이 되면 3명의 학생은 삼총사라고 합니다. 
예를 들어, 5명의 학생이 있고, 각각의 정수 번호가 순서대로 -2, 3, 0, 2, -5일 때, 
첫 번째, 세 번째, 네 번째 학생의 정수 번호를 더하면 0이므로 세 학생은 삼총사입니다. 
또한, 두 번째, 네 번째, 다섯 번째 학생의 정수 번호를 더해도 0이므로 세 학생도 삼총사입니다. 
따라서 이 경우 한국중학교에서는 두 가지 방법으로 삼총사를 만들 수 있습니다.

한국중학교 학생들의 번호를 나타내는 정수 배열 number가 매개변수로 주어질 때, 
학생들 중 삼총사를 만들 수 있는 방법의 수를 return 하도록 solution 함수를 완성하세요.
"""
from itertools import permutations # 순열
from itertools import combinations # 조합

from itertools import product # 중복 순열
from itertools import combinations_with_replacement # 중복 조합

def solution(number):
    answer = 0
    result = list(combinations(number, 3))
    for i in result: 
        if sum(i) == 0:
            answer += 1    
    return answer

number = [-1, 1, -1, 1]
result = solution(number)
print(result)







from itertools import permutations # 순열
from itertools import combinations # 조합

from itertools import product # 중복 순열
from itertools import combinations_with_replacement # 중복 조합

a = ["A","B","C"]

result = list(permutations(a, 2))
print(result)
result = list(combinations(a, 2))
print(result)

result = list(product(a, repeat = 2))
print(result)

result = list(combinations_with_replacement(a, 2))
print(result)