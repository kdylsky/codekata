"""
문제풀이
1. 전체길이가 짝수인지 홀수인지 판단 후 홀수라면 바로 return 0 
2. stack을 만들어서 s의 첫번째 값 추가
3. stack의 길이를 판단해서 0이라면 바로 추가 아니라면 top과 같은지 판단, 만약 같다면, continue와 stack에서 pop
4. 같지 않다면 stack에 넣어준다.
5. for문이 완료 후 stack에 남아있다면 return 0 아니라면 return 1 
"""
def solution(s):
    if len(s)%2 ==0:
        stack = []
        stack.append(s[0])
        for j in s[1:]:
            if len(stack) != 0:
                if stack[-1] == j:
                    stack.pop()
                    continue
                else:
                    stack.append(j)
            else:
                stack.append(j)
        
        if len(stack) == 0:
            return 1
        else :
            return 0
    else:
        return 0
