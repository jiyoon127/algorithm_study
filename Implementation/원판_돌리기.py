import sys
from collections import deque
input = sys.stdin.readline

def turn(x, d, k):
    global cur_remain

    for target in range(x, n + 1, x):
        if d == 0:
            graph[target - 1] = graph[target - 1][-k:] + graph[target - 1][:-k]
        else:
            graph[target - 1] = graph[target - 1][k:] + graph[target - 1][:k]

    is_removed = False

    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not graph[i][j]: continue
            cur_removed = False
            q = deque([(i, j)])

            while q:
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx = x + dx
                    ny = (y + dy) % m
                    if 0 <= nx < n and not visited[nx][ny] and graph[nx][ny] == graph[i][j] and (nx, ny) != (i, j):
                        visited[nx][ny] = 1
                        is_removed, cur_removed = True, True
                        cur_remain -= 1
                        graph[nx][ny] = 0
                        q.append((nx, ny))

            if cur_removed:
                graph[i][j] = 0
                cur_remain -= 1
                visited[i][j] = 1

    if not is_removed:
        if not cur_remain: return
        avg = sum(map(sum, graph)) / cur_remain
        for i in range(n):
            for j in range(m):
                if graph[i][j]:
                    if graph[i][j] < avg: graph[i][j] += 1
                    elif graph[i][j] > avg: graph[i][j] -= 1

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cur_remain = m * n

for _ in range(t):
    x, d, k = map(int, input().split())
    turn(x, d, k)

print(sum(map(sum, graph)))
