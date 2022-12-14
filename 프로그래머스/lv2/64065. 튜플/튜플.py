def solution(s):
    p = ""
    result = []
    stack = []
    for x in s[2:-1]:
        if x.isdigit():
            p+=x
        elif len(p) != 0 and x == "," or x == "}":
            stack.append(p)
            p = ""
        elif x == "{":
            result.append(stack)
            stack = []
    if len(stack) != 0:
        result.append(stack)
    
    answer = []
    k = sorted(result, key=lambda x : len(x))
    for i in k:
        for j in i:
            if j not in answer:
                answer.append(j)

    return list(map(int, answer))