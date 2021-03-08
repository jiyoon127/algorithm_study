# 막힐때 까지 한번에 이동하는 점이 포인트
# 최소 이동 횟수를 구해야 하므로 bfs

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
    row = list(input().strip())
    graph.append(row)
    if "O" in row:
        whole = (i, row.index("O"))
    if "R" in row:
        red = (i, row.index("R"))
    if "B" in row:
        blue = (i, row.index("B"))

def move(x, y, dx, dy):
    moved = 0
    while graph[x + dx][y + dy] != "#" and graph[x][y] != "O":
        x += dx
        y += dy
        moved += 1
    return x, y, moved

def bfs():
    q = deque()
    q.append((red, blue, 1))
    visited = [(red[0], red[1], blue[0], blue[1])]

    while q:
        r, b, depth = q.popleft()
        if depth > 10: break

        rx, ry = r
        bx, by = b

        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nrx, nry, rmoved = move(rx, ry, dx, dy)
            nbx, nby, bmoved = move(bx, by, dx, dy)

            if graph[nbx][nby] != "O":
                if graph[nrx][nry] == "O":
                    print(depth)
                    return

                if (nrx, nry) == (nbx, nby):
                    if rmoved > bmoved:
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy

                if (nrx, nry, nbx, nby) not in visited:
                    visited.append((nrx, nry, nbx, nby))
                    q.append(((nrx, nry), (nbx, nby), depth + 1))

    print(-1)

bfs()
