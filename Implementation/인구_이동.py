import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()
next_q = deque()
tot_move = 0

def bfs(i, j):
    _sum = graph[i][j]
    union = [(i, j)]
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and l <= abs(graph[x][y] - graph[nx][ny]) <= r and not visited[nx][ny]:
                q.append((nx, ny))
                union.append([nx, ny])
                _sum += graph[nx][ny]
                visited[nx][ny] = True
    if len(union) >= 2:
        ppl = _sum // len(union)
        for x, y in union:
            graph[x][y] = ppl
            next_q.append((x, y))
        return True
    return False

for i in range(n):
    for j in range(n):
        next_q.append((i, j))

while True:
    visited = [[False] * n for _ in range(n)]
    is_moved = False
    for _ in range(len(next_q)):
        i, j = next_q.popleft()
        if not visited[i][j]:
            visited[i][j] = True
            if bfs(i, j): is_moved = True
    if not is_moved: break
    tot_move += 1

print(tot_move)
