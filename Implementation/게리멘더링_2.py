import sys
input = sys.stdin.readline

def divide(x, y, d1, d2, graph):
    new_graph = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            new_graph[i][j] = graph[i][j]

    div_pop = [0] * 5

    for i in range(d1 + 1):
        new_graph[x + i][y - i] = 0
        new_graph[x + d2 + i][y + d2 - i] = 0

    for i in range(d2 + 1):
        new_graph[x + i][y + i] = 0
        new_graph[x + d1 + i][y - d1 + i] = 0

    for i in range(x + 1, x + d1 + d2):
        is_boundary = False
        for j in range(1, n + 1):
            if not new_graph[i][j]: is_boundary = not is_boundary
            if is_boundary: new_graph[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i < x + d1 and j <= y and new_graph[i][j]: div_pop[0] += new_graph[i][j]
            elif i <= x + d2 and y < j and new_graph[i][j]: div_pop[1] += new_graph[i][j]
            elif x + d1 <= i and j < y - d1 + d2 and new_graph[i][j]: div_pop[2] += new_graph[i][j]
            elif x + d2 < i and y - d1 + d2 <= j and new_graph[i][j]: div_pop[3] += new_graph[i][j]

    div_pop[4] = tot_pop - sum(div_pop)
    return max(div_pop) - min(div_pop)

n = int(input())
graph = [([0] + list(map(int, input().split()))) for _ in range(n)]
graph = [[0] * (n + 1)] + graph

tot_pop = sum(map(sum, graph))
_min = int(1e9)

for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    _min = min(_min, divide(x, y, d1, d2, graph))

print(_min)
