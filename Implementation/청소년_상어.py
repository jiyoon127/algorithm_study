import sys
from copy import deepcopy
input = sys.stdin.readline

fishes = []
graph = []
ans = -int(1e9)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
for i in range(4):
    row = list(map(int, input().split()))
    graph.append([])
    for j in range(0, 8, 2):
        graph[i].append([row[j], row[j + 1]])
        fishes.append((row[j], row[j + 1], i, j // 2))
fishes.sort()

fishes[graph[0][0][0] - 1] = ()
ate = graph[0][0][0]
graph[0][0][0] = -1


def turn(x, y, direct):
    for _ in range(8):
        nx = x + dx[(direct - 1) % 8]
        ny = y + dy[(direct - 1) % 8]
        if 0 <= nx < 4 and 0 <= ny < 4 and graph[nx][ny][0] != -1:
            return nx, ny, direct if direct != 0 else 8
        else:
            direct = (direct + 1) % 8
    return x, y, False


def move_fish():
    for i in range(16):
        if fishes[i]:
            cur, direct, x, y = fishes[i]
            nx, ny, n_direct = turn(x, y, direct)

            if not n_direct: continue
            if graph[nx][ny][0]:
                og, og_direct = graph[nx][ny]
                graph[nx][ny] = [cur, n_direct]
                graph[x][y] = [og, og_direct]
                fishes[og - 1] = (og, og_direct, x, y)
            else:
                graph[nx][ny] = [cur, n_direct]
                graph[x][y] = [0, 0]
            fishes[i] = (cur, n_direct, nx, ny)


def simulate(x, y, direct, ate):
    global ans, fishes, graph
    move_fish()

    graph[x][y] = [0, 0]
    while True:
        nx = x + dx[direct - 1]
        ny = y + dy[direct - 1]
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            ans = max(ans, ate)
            return
        if not graph[nx][ny][0]:
            x, y = nx, ny
            continue

        new_graph, new_fishes = deepcopy(graph), deepcopy(fishes)
        prey, p_direct = graph[nx][ny]
        fishes[prey - 1] = ()
        graph[nx][ny][0] = -1
        simulate(nx, ny, p_direct, ate + prey)
        graph = new_graph
        fishes = new_fishes
        x, y = nx, ny


simulate(0, 0, graph[0][0][1], ate)
print(ans)
