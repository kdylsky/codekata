def solution(s):
    try:
        stack = []
        for i in s:
            if i == ")":
                stack.pop()
            else:
                stack.append(i)
        if len(stack) > 0:
            return False
        return True
    except:
        return False       