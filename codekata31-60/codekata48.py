"""
서울에서 김서방 찾기

문제 설명
String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, 
"김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. 
seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
"""

from curses.ascii import isdigit


def solution(seoul):    
    for i,j in enumerate(seoul):
        if j == "Kim":
            return f"김서방은 {i}에 있다" 
       
def solution(seoul):
    pos = seoul.index("Kim")
    return f"김서방은 {pos}에 있다"

    
"""
문자열 다루기 기본

문제 설명
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
"""

def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if not i.isdigit():
                return False
        else:
            return True
    else:
        return False
    
def solution(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6 



"""
문자열 내림차순으로 배치하기
문제 설명
문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

"""

def solution(s):
    temp = sorted(s, key= lambda x : ord(x),reverse=True)
    
    return "".join(temp)


"""
문자열 내 p와 y의 개수
문제 설명
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

1.문자열을 하나로 통일 해준다.
2.count라이브러리를 이용해서 숫자를 세준다.

"""
from collections import Counter
def solution(s):
    s = s.lower()
    temp = Counter(s)
    if temp.get("p") == temp.get("y"):
        return True
    else:
        return False

def solution(s):
    return s.lower().count('p') == s.lower().count('y')
