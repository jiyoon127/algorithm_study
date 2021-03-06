import sys
input = sys.stdin.readline

def move(t, graph, column):
    global point

    if not graph: graph.append([0, 0, 0, 0])
    final_positions = []
    cur = len(graph) - 1
    while cur >= 0:
        row = graph[cur]
        if t == 1:
            if not row[column]: final_positions = [(cur, column)]
            else: break
        elif t == 2:
            if (row[column], row[column + 1]) == (0, 0):
                final_positions = [(cur, column), (cur, column + 1)]
            else: break
        elif t == 3:
            if cur >= 1 and (row[column], graph[cur - 1][column]) == (0, 0):
                final_positions = [(cur,  column), (cur - 1, column)]
            else: break

        cur -= 1

    if not final_positions:
        graph.append([0, 0, 0, 0])
        if t == 1: final_positions = [(-1, column)]
        elif t == 2:
            final_positions = [(-1, column), (-1, column + 1)]
        else:
            if graph[-2][column]: graph.append([0, 0, 0, 0])
            final_positions = [(-2, column), (-1, column)]

    for x, y in final_positions:
        graph[x][y] = 1
        if sum(graph[x]) == 4:
            graph.pop(x)
            point += 1

    while len(graph) > 4:
        graph.pop(0)

n = int(input())
steps = [list(map(int, input().split())) for _ in range(n)]
green, blue = [], []
point = 0

for step in steps:
    t, x, y = step
    move(t, green, y)
    if t == 1: move(t, blue, x)
    elif t == 2: move(3, blue, x)
    else: move(2, blue, x)

print(point)
print(sum(map(sum, green)) + sum(map(sum, blue)))
