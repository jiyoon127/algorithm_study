# bruth force------------------------------------------------------------------------------------------------
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
max_val = -int(1e9)
tetrominoes = [
    [(2, 0), (1, 0), (0, 0), (0, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(1, 0), (0, 0), (0, 1), (0, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(2, 0), (1, 0), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 1)],
    [(2, 0), (1, 0), (1, 1), (0, 0)],
    [(0, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 1), (1, 1), (1, 0), (2, 1)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)]
]

def check_range(tetromino, i, j):
    cur_val = 0
    for dx, dy in tetromino:
        nx = i + dx
        ny = j + dy
        if 0 <= nx < n and 0 <= ny < m:
            cur_val += graph[nx][ny]
        else: return False
    return cur_val

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        for tetromino in tetrominoes:
            cur = check_range(tetromino, i, j)
            if cur: max_val = max(max_val, cur)
            else: continue

print(max_val)
