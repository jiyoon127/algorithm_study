import sys
input = sys.stdin.readline

def turnCctv(cur, graph):
    global _min
    if cur == len(cctvs):
        cnt = 0
        for row in graph:
            cnt += row.count(0)
        _min = min(_min, cnt)
        return

    _type, x, y = cctvs[cur]
    for direct in directions[_type]:
        new_graph = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if graph[i][j]: new_graph[i][j] = graph[i][j]

        for i in direct:
            nx = x + dx[i]
            ny = y + dy[i]

            while 0 <= nx < n and 0 <= ny < m:
                if new_graph[nx][ny] == 6: break
                if not new_graph[nx][ny]: new_graph[nx][ny] = "#"
                nx += dx[i]
                ny += dy[i]
        turnCctv(cur + 1, new_graph)

n, m = map(int, input().split())
graph = []
cctvs = []
directions = [[0],
         [[0], [1], [2], [3]],
         [[0, 2], [1, 3]],
         [[0, 1], [1, 2], [2, 3], [3, 0]],
         [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
         [[0, 1, 2, 3]]
         ]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
_min = n * m

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j, cctv in enumerate(row):
        if cctv not in (0, 6): cctvs.append((cctv, i, j))

turnCctv(0, graph)

print(_min)
