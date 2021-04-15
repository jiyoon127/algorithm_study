import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def storm(s_len):
    if s_len == 1: turned = graph.copy()
    else:
        turned = [[0] * _len for _ in range(_len)]
        for i in range(0, _len, s_len):
            for j in range(0, _len, s_len):
                for r in range(s_len):
                    for c in range(s_len):
                        nr = i + c
                        nc = j + s_len - r - 1
                        turned[nr][nc] = graph[i + r][j + c]

    new_graph = [[0] * _len for _ in range(_len)]
    for i in range(_len):
        for j in range(_len):
            if not turned[i][j]: continue
            cnt = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni = i + dx
                nj = j + dy
                if 0 <= ni < _len and 0 <= nj < _len and turned[ni][nj]: cnt += 1
            if cnt < 3: new_graph[i][j] = turned[i][j] - 1
            else: new_graph[i][j] = turned[i][j]

    return new_graph

def dfs(x, y):
    size = 1
    graph[x][y] = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < _len and 0 <= ny < _len and graph[nx][ny]:
            size += dfs(nx, ny)

    return size

n, q = map(int, input().split())
_len = pow(2, n)
graph = [list(map(int, input().split())) for _ in range(_len)]
big_chunk = 0

for step in list(map(int, input().split())):
    graph = storm(pow(2, step))

print(sum(map(sum, graph)))

for i in range(_len):
    for j in range(_len):
        if graph[i][j]:
            big_chunk = max(big_chunk, dfs(i, j))

print(big_chunk)
