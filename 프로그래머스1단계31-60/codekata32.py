def solution(board, moves):
    stack = []
    
    if len(board) == 0:
        return 0
    
    if len(moves) == 0:
        return 0
    
    a = {i+1:[] for i in range(len(board))}
    count = 0
    
    for i in range(len(board)):
        for k, j in enumerate(board[i]):
            if j != 0:    
                a[k+1].append(j)
    
    if len(moves) == 0:
        return 0
    
    if not any([len(a[i]) for i in a]):
        return 0
    
    stack.append(a[moves.pop(0)].pop(0))
    
    for i in moves:    
        if len(a[i]) != 0:
            if stack[-1] == a[i][0]:
                count += 2
                del stack[-1]
                del a[i][0]
                # stack.pop(-1)
                # a[i].pop(0)
            else:
                stack.append(a[i][0])
                del a[i][0]
                # a[i].pop(0)    
    
    return count

# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# moves = [1,5,3,5,1,2,1,4]
board = []
moves = []
a = solution(board, moves)
print(a)