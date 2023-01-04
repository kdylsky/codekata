from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    temp = []
    temp.append(queue.popleft())
    cnt = 0
    while queue:    
        for i in queue:
            if temp[0] <= i:
                cnt+=1
            elif temp[0] > i:
                cnt+=1
                break
        
        temp.pop()
        temp.append(queue.popleft())
        answer.append(cnt)
        cnt = 0
    
    return answer + [0]