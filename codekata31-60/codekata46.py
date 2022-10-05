"""
약수의 합

1부터 정수 n까지 반복문을 돌면서 해당 변수로 n을 나누었으 때, 나머지가 0이 되는 경우가 n의 약수가 된다.
그렇기 때문에 0이 돠는 변수를 리스트로 구한 후 리스트의 메서드인 sum()을 이용해서 return 해준다.
"""



def solution(n):
    return sum([i for i in range(1, n+1) if n % i == 0])


"""
시저 암호

문자열 s를 for문을 돌면서 요소 하나씩 가지고 온다.
해당 요소를 ord()로 정수값으로 변경후 n을 더하고 다시 chr()로 변경해준다.
Z가 들어오는 경우라면 A부터 시작하게 한다.
z가 들어오는 경우라면 a부터 시작하게 한다.
"""

from curses.ascii import islower, isupper
def solution(s, n):
    answer = ''
    limit_z = ord("z")
    limit_Z = ord("Z")    
    
    for i in s:
        if i == "z":
            answer+= chr(ord("a") + n-1)
        elif i == "Z":
            answer+= chr(ord("A") + n-1)
        elif i == " ":
            answer += " "
        else:
            temp = ord(i) + n
            if islower(i):
                if temp > limit_z :
                    answer += chr(ord("a") + (temp-limit_z) -1)
                else:
                    answer+= chr(ord(i) + n)
            elif isupper(i):     
                if temp > limit_Z:
                    answer += chr(ord("A") + (temp-limit_Z) -1)
                else:        
                    answer+= chr(ord(i) + n)
    
    return answer



"""
문자열을 정수로 바꾸기
문제 설명
문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

제한 조건
s의 길이는 1 이상 5이하입니다.
s의 맨앞에는 부호(+, -)가 올 수 있습니다.
s는 부호와 숫자로만 이루어져있습니다.
s는 "0"으로 시작하지 않습니다.

"""
def solution(s):
    return int(s)

def solution(s):
    answer = 1
    k = len(s)
    if s[0] == "-":
        answer *= -1
        k = k-1
        s = s[1:]
    
    sum = 0
    for i ,j in zip(s, range(k-1,-1,-1)):
        sum += (10**j * int(i))

    return answer * sum

"""
수박수박수박수박수박수?

문제 설명
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, 
solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
"""

def solution(n):
    a = "수박"
    answer = ''
    c = n // len(a)
    
    if n % len(a) == 0:
        answer += a*c 
    else:
        answer += a*c
        answer += "수"

    return answer


