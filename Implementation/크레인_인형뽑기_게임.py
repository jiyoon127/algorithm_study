def solution(board, moves):
    answer = 0
    got = []
    popped = 0
    
    for move in moves:
        for i in range(len(board)):
            j = move - 1
            if board[i][j]:
                cur = board[i][j]
                board[i][j] = 0
                if got and got[-1] == cur:
                    got.pop()
                    popped += 2
                else: got.append(cur)
                break
    return popped
