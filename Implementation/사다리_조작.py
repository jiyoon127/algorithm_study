# pypy 3

import sys
input = sys.stdin.readline

def check():
    for col in range(n):
        row = 0
        cur = (row, col)
        while cur[0] < h:
            if graph[cur[0]][cur[1]]:
                cur = (cur[0], cur[1] + 1)
            elif cur[1] > 0 and graph[cur[0]][cur[1] - 1]:
                cur = (cur[0], cur[1] - 1)
            cur = (cur[0] + 1, cur[1])
        if cur[1] != col: return False

    return True

def putLine(cnt, x, y):
    global _min
    if check():
        _min = min(_min, cnt)
        return

    elif cnt == 3 or _min <= cnt: return

    for i in range(x, h):
        tmp = y if i == x else 0
        for j in range(tmp, n - 1):
            if not graph[i][j] and not graph[i][j + 1]:
                graph[i][j] = 1
                putLine(cnt + 1, i, j + 2)
                graph[i][j] = 0

n, m, h = map(int, input().split())
graph = [[0] * n for _ in range(h)]
_min = 4

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = 1

putLine(0, 0, 0)

print(_min if _min <= 3 else -1)
