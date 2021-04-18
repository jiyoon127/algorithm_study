import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    visited[i][j] = 1
    union = [(i, j)]
    _sum = graph[i][j]
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and l <= abs(graph[x][y] - graph[nx][ny]) <= r and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                union.append((nx, ny))
                _sum += graph[nx][ny]

    if len(union) > 1:
        avg = _sum // len(union)
        for x, y in union:
            graph[x][y] = avg
            _next.append((x, y))
        return True

    return False

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = []
_next = deque()
q = deque()
cnt = 0

for i in range(n):
    for j in range(n):
        _next.append((i, j))

while True:
    is_moved = False
    visited = [[0] * n for _ in range(n)]

    for _ in range(len(_next)):
        i, j = _next.popleft()
        if not visited[i][j]:
            if bfs(i, j): is_moved = True

    if not is_moved:
        print(cnt)
        break

    cnt += 1
