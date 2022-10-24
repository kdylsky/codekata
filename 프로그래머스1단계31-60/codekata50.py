"""
크레인 인형뽑기 게임
[0,0,0,0,0]
[0,0,1,0,3]
[0,2,5,0,1]
[4,2,4,4,2]
[3,5,1,3,1]]
"""


#[[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
#[[0, 0, 0, 4, 3], [0, 0, 2, 2, 5], [0, 1, 5, 4, 1], [0, 0, 0, 4, 3], [0, 3, 1, 2, 1]]
def solution(board, moves):
    answer = 0
    stack = []
    cnt = 0
    result = []
    for i in range(len(board)):
        temp = []
        for i,j in enumerate(board):
            temp.append(board[i][cnt])
        result.append(temp)
        cnt += 1
    
    for i in moves:
        for j in result[i-1]: 
            if j != 0:
                if stack and stack[-1] == j:
                    answer += 2
                    stack.pop(-1)
                    break
                stack.append(j)
                break
        result[i-1][result[i-1].index(j)] = 0
    return answer 
        


def solution(board, moves):
    stacklist = []
    answer = 0
    
    for move in moves:
        for i in range(len(board)):
            # board의 각 요소의 move-1에 해당하는 값이 무었인지 확인한다.
            # 0이 아니라면 해당 요소가 stacklist에 추가되는 것이다.
            # 그리고 해당 요소를 0으로 바꾸어 준다.
            if board[i][move-1] != 0:
                stacklist.append(board[i][move-1])
                board[i][move-1] = 0
 
                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
# board = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
# moves = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4]
result = solution(board, moves)
# print(result)
