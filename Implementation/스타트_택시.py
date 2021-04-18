import sys
from collections import deque
input = sys.stdin.readline

def find_cus(i, j):
    global tx, ty, oil, is_impossible

    if (i, j) in cus:
        target = (i, j, 0)
    else:
        q = deque()
        visited = [[0] * (n + 1) for _ in range(n + 1)]
        target = ()
        q.append((i, j, 0))
        visited[i][j] = 1
        while q:
            x, y, cnt = q.popleft()
            if target and cnt == target[2]: break

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                if 0 < nx <= n and 0 < ny <= n and not visited[nx][ny] and not graph[nx][ny]:
                    visited[nx][ny] = 1
                    if (nx, ny) in cus:
                        if not target: target = (nx, ny, cnt + 1)
                        else: target = min([target, (nx, ny, cnt + 1)], key = lambda x: (x[0], x[1]))
                    q.append((nx, ny, cnt + 1))

        if not target or oil < target[2]: return False
        oil -= target[2]

    q = deque()
    q.append((target[0], target[1], 0))
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    destination = cus[(target[0], target[1])]

    while q:
        x, y, cnt = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 < nx <= n and 0 < ny <= n and not visited[nx][ny] and not graph[nx][ny]:
                visited[nx][ny] = 1
                if (nx, ny) == destination:
                    if oil < cnt + 1: return False
                    else:
                        tx, ty, oil = nx, ny, oil + cnt + 1
                        del cus[(target[0], target[1])]
                        return True
                q.append((nx, ny, cnt + 1))

n, m, oil = map(int, input().split())
graph = [[0]]
for _ in range(n):
    graph.append([0] + list(map(int, input().split())))

tx, ty = map(int, input().split())
cus = {}
is_impossible = False

for _ in range(m):
    r, c, dr, dc = map(int, input().split())
    cus[(r, c)] = (dr, dc)

for _ in range(m):
    if not find_cus(tx, ty):
        oil = -1
        break

print(oil)
