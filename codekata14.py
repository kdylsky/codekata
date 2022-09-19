def solution(arr):
    queue = []
    stack = []
    stack.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] in stack:
            continue
        queue.append(stack.pop())
        stack.append(arr[i])
    
    queue.append(stack.pop())
    
    return queue

arr = [4,4,4,3,3,2]
result = solution(arr)
print(result)


def no_continuous(s):
    a = []
    for i in s:
        if i in a[-1:] : 
            continue
        a.append(i)
    return a

s = [4,4,4,3,3]
result = no_continuous(s)
print(result)