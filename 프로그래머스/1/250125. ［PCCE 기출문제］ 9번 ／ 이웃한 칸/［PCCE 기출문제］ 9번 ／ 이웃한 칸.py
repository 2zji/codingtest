def solution(board, h, w):
    n = len(board)
    answer = 0
    color = board[h][w]
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]
        
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h_check][w_check] == color:
                answer += 1
    
    return answer