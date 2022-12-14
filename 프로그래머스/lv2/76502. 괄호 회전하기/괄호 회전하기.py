"""
문제풀이
1.올바른 괄호인지를 판단하는 함수 is_vaild()를 선언
2.deque를 이용해서 길이만큼 돌면서 빼고 뒤에 다시 더해준다.
3.그리고 is_valid()로 판단 True라면 cnt+1 아니라면 continue
"""
from collections import deque

def is_vaild(s):
    stack = []
    value = {
        "}" : "{",
        "]" : "[",
        ")" : "("
    }
    try:
        for i in s:
            if i =="{" or i =="[" or i =="(":
                stack.append(i)
            else:
                if stack[-1] == value[i]:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
    except:
        return False        

def solution(s):
    cnt = 1 if is_vaild(s) else 0
    deque_list = deque(s)

    for _ in range(1, len(s)):
        x = deque_list.popleft()
        deque_list.append(x)
        if is_vaild(deque_list):
            cnt+=1
    return cnt