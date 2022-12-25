from collections import deque


def bfs(graph, v, b, visited):
    temp = []
    queue = deque()
    # 시작노드를 q에 넣어준다.
    queue.append(v)
    # 시작노드를 방문 처리해준다.
    visited[v] = True
    
    # queue가 빌 때 까지 반복한다.
    while queue:
        # queue에서 하나의 원소를 꺼낸다.
        v = queue.popleft()
        temp.append(v)
        
        # 아직 방문하지 않는 원소가 있다면 해당 원소들을 모두 queue에 삽입해준다.
        # 그리고 방문 처리를 해준다.
        
        for i in graph[v]:            
            if i == b:
                continue
            else:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
    return temp


def solution(n, wires):    
    graph = [[]*i for i in range(n+1)]
    for node, value  in wires:
        graph[node].append(value)
        graph[value].append(node)        
    temp = []
    for front, back in wires:
        visited = [False]*(n+1)
        x = bfs(graph, front, back, visited)
        y = n - len(x)
        temp.append(abs(len(x)-y))
    return min(temp)