# python3----------------------------------------------------------------------------------------------------------------------------------------------------------

import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
graph = []
cleaner = []
result = 0

for i in range(r):
    row = list(map(int, input().split()))
    graph.append(row)
    result += sum(row)
    if -1 in row: cleaner.append(i)

def spreading():
    new_graph = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j]:
                new_graph[i][j] = graph[i][j]
    for x in range(r):
        for y in range(c):
            if graph[x][y] >= 5:
                spreaded = 0
                spread = graph[x][y] // 5
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        new_graph[nx][ny] += spread
                        spreaded += 1
                new_graph[x][y] -= spread * spreaded
    return new_graph

def cleaning():
    global result
    upper, under = cleaner
    result -= graph[upper - 1][0] + graph[under + 1][0]

    for i in range(upper - 2, -1, -1):
        graph[i + 1][0] = graph[i][0]
    for i in range(under + 2, r):
        graph[i - 1][0] = graph[i][0]

    for i in range(1, c):
        graph[0][i - 1] = graph[0][i]
        graph[-1][i - 1] = graph[-1][i]

    for i in range(1, upper + 1):
        graph[i - 1][-1] = graph[i][-1]
    for i in range(r - 2, under - 1, -1):
        graph[i + 1][-1] = graph[i][-1]

    for i in range(c - 2, 0, -1):
        graph[upper][i + 1] = graph[upper][i]
        graph[under][i + 1] = graph[under][i]
    graph[upper][1] = 0
    graph[under][1] = 0
for _ in range(t):
    graph = spreading()
    cleaning()

print(result + 2)



# pypy 3----------------------------------------------------------------------------------------------------------------------------------------------------------

import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
graph = []
cleaner = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = 0

for i in range(r):
    row = list(map(int, input().split()))
    graph.append(row)
    result += sum(row)
    if -1 in row: cleaner.append(i)

def spreading():
    new_graph = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j]:
                new_graph[i][j] = graph[i][j]
    for x in range(r):
        for y in range(c):
            cur_dust = graph[x][y]
            if cur_dust >= 5:
                spreaded = 0
                spread = cur_dust // 5
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        new_graph[nx][ny] += spread
                        spreaded += 1
                new_graph[x][y] -= spread * spreaded
    return new_graph

def cleaning():
    global result
    upper, under = cleaner
    result -= graph[upper - 1][0] + graph[under + 1][0]

    for i in range(upper - 2, -1, -1):
        graph[i + 1][0] = graph[i][0]
    graph[0] = graph[0][1:] + [0]
    for i in range(1, upper + 1):
        graph[i - 1][-1] = graph[i][-1]
    graph[upper] = [-1, 0] + graph[upper][1:-1]

    for i in range(under + 2, r):
        graph[i - 1][0] = graph[i][0]
    graph[r - 1] = graph[r - 1][1:] + [0]
    for i in range(r - 2, under - 1, -1):
        graph[i + 1][-1] = graph[i][-1]
    graph[under] = [-1, 0] + graph[under][1:-1]

for _ in range(t):
    graph = spreading()
    cleaning()

print(result + 2)
