import sys
input = sys.stdin.readline

def checkLoad(road):
    global roads
    new_road = road.copy()
    ramps = []
    left_h = road[0]
    for i in range(1, n):
        right_h = road[i]
        if abs(right_h - left_h) > 1: return
        elif left_h < right_h:
            if not 0 <= i - l < n: return
            for j in range(1, l + 1):
                if road[i - j] != left_h or i - j in ramps: return
            ramps.append(i - j)
            left_h = right_h

        elif left_h > right_h:
            if not 0 <= i + l - 1 < n: return
            for j in range(0, l):
                if road[i + j] != right_h or i + j in ramps: return
            ramps.append(i + j)
            left_h = right_h
            
    roads += 1

def turnGraph(graph):
    new_graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[j][n - 1 - i] = graph[i][j]

    return new_graph

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
roads = 0

for t in range(2):
    for i in range(n):
        row = graph[i]
        if row.count(row[0]) == n:
            roads += 1
            continue
        else: checkLoad(row)

    if t == 0: graph = turnGraph(graph)

print(roads)
