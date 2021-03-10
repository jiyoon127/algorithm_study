# pypy 3

import sys
input = sys.stdin.readline


def followLine():
    for line in range(1, n + 1):
        cur = line
        for i in range(1, h + 1):
            if graph[i][cur]: cur += 1
            elif cur > 1 and graph[i][cur - 1]: cur -= 1
        if cur != line: return False

    return True

def addLine(cnt, x, y):
    global result
    if followLine():
        result = min(result, cnt)
        return
    elif cnt == 3 or result <= cnt: return

    for i in range(x, h+1):
        k = y if i == x else 1
        for j in range(k, n):
            if not graph[i][j] and not graph[i][j + 1]:
                graph[i][j] = 1
                addLine(cnt + 1, i, j + 2)
                graph[i][j] = False

n, m, h = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(h + 1)]
INF = int(1e9)
result = INF

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

addLine(0, 1, 1)

print(result if result != INF else -1)
