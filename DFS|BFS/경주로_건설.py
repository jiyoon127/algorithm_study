# 단순 visited 체크론 시간초과 난다. min_cost 체크해 최소 금액을 맞출수 없는 경로는 빠르게 버려야 함

from collections import deque

def bfs(x, y, _sum, direct, board):
    min_cost = [[int(1e9)] * len(board) for _ in range(len(board))]
    q = deque([(x, y, _sum, direct)])
    
    min_cost[0][0] = 0
    while q:
        x, y, _sum, direct = q.popleft()
        for i, (dx, dy) in enumerate([(0, 1), (0, -1),(1, 0), (-1, 0)]):
            nx = x + dx
            ny = y + dy
            new_sum = _sum + 600 if i != direct else _sum + 100
            
            if 0 <= nx < len(board) and 0 <= ny < len(board) and not board[nx][ny] and min_cost[nx][ny] > new_sum:
                min_cost[nx][ny] = new_sum
                q.append((nx, ny, new_sum, i))
                
    return min_cost[len(board) - 1][len(board) - 1]

def solution(board):
    
    return min(bfs(0, 0, 0, 0, board), bfs(0, 0, 0, 2, board))
