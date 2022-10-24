import math

def solution(progresses, speeds):
    days = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    
    max     = days[0]
    count   = 0
    anwser  = []
    
    for i in days:
        if max >= i : 
            count += 1
            continue 
        else:
            max = i
            anwser.append(count)
            count = 1
    
    anwser.append(count)
    return anwser



def solution(progresses, speeds):
    days = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    stack = []
    answer = []
    queue = []
    for i in days:
        if len(stack) == 0:
            stack.append(i)
        elif stack[0] < i:
            queue.append(stack.pop())
            answer.append(len(queue))
            queue.clear()
            stack.append(i)
        else:
            queue.append(i)
    
    queue.append(stack.pop())
    answer.append(len(queue))    
    
    return answer
    
    
    
    
def solution(progresses, speeds):
    days = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    stack = []
    answer = []
    queue = []
    
    stack.append(days[0])
    for i in range(1, len(days)):
        if stack[0] >= days[i]:
            queue.append(days[i])
        else:
            queue.append(stack.pop())
            answer.append(len(queue))
            queue.clear()
            stack.append(i)
    queue.append(stack.pop())
    answer.append(len(queue))

    return answer 


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

# result = solution(progresses, speeds)
# print(result)

a = dict(zip(progresses, speeds))
print(a)