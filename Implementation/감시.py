import sys
input = sys.stdin.readline

def dfs(cur, graph):
    global result
    if cur == len(cams):
        cnt = 0
        for row in graph:
            cnt += row.count(0)
        result = min(result, cnt)
        return

    type, (x, y) = cams[cur]
    for direct in turns[type]:
        new_graph = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if graph[i][j]: new_graph[i][j] = graph[i][j]

        for i in direct:
            nx = x + dx[i]
            ny = y + dy[i]

            while 0 <= nx < n and 0 <= ny < m:
                if new_graph[nx][ny] == 6: break
                if not new_graph[nx][ny]:
                    new_graph[nx][ny] = "#"

                nx += dx[i]
                ny += dy[i]

        dfs(cur + 1, new_graph)

n, m = map(int, input().split())
graph = []
cams = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
turns = [0,
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]
result = int(1e9)

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j, cam in enumerate(row):
        if cam not in (0, 6): cams.append((cam, (i, j)))

dfs(0, graph)

print(result)
