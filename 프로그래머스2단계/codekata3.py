"""
문제 설명
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 
단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

s는 길이 1 이상 200 이하인 문자열입니다.
s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
숫자는 단어의 첫 문자로만 나옵니다.
숫자로만 이루어진 단어는 없습니다.
공백문자가 연속해서 나올 수 있습니다.
"""

"""
문제풀이
1. 먼저 split()을 이용해서 해당 문자열을 각 단어로 이루어진 리스트로 만든다.
2. 공백문자가 연속으로 나올 수 있기 떼문에, 만약 길이가 0이라면 결과 리스트에 ""을 append
3. 해당 리스트를 for문을 돌면서 첫번째 문자가 문자라면 대문자로 변경
4, 그 이후의 모든 문자열은 소문자로 변경
"""

def solution(s):
    new_lst = s.split(" ")
    temp =[]
    for str in new_lst:
        answer=""
        if len(str) > 0:
            if str[0].isdigit():
                answer+=str[0]
            else:
                answer+=str[0].upper()
        else:
            temp.append("")
            continue
        for i in str[1:]:
            answer+= i.lower() 
        temp.append(answer)
    return " ".join(temp)
    
s = "  for add the  last       week"
result = solution(s)
print(result)