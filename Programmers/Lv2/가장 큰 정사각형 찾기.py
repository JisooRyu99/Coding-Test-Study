# https://school.programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):

    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j]==1:
                board[i][j]=min(board[i-1][j-1],board[i][j-1],board[i-1][j])+1
    
    answer = max(max(board))
    return answer**2