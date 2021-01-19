import sys
input = sys.stdin.readline

ans = 0
r, c, m = map(int, input().split())
graph = [[0] * c for _ in range(r)]
for _ in range(m):
  i, j, s, d, z = map(int, input().split())
  graph[i-1][j-1] = [s, d, z]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def catch(r, c):
  for j in range(r):
    if graph[j][c]:
      weight = graph[j][c][2]
      graph[j][i] = 0
      return weight
  return 0

def turn(direct):
  if direct == 1: direct = 2
  elif direct == 2: direct = 1
  elif direct == 3: direct = 4
  elif direct == 4: direct = 3
  return direct
  
def move(i, j, shark, new_graph):
  s, d, z = shark
  for _ in range(s):
    nx = i + dx[d-1]
    ny = j + dy[d-1]
    if 0 <= nx < r and 0 <= ny < c: 
      i, j = nx, ny
      continue
    d = turn(d)
    i, j = i + dx[d-1], j + dy[d-1]

  if not new_graph[i][j] or (new_graph[i][j] and new_graph[i][j][2] < z):
    new_graph[i][j] = [s, d, z]

for i in range(c):
  ans += catch(r, i)
  new_graph = [[0] * c for _ in range(r)]
  for x in range(r):
    for y in range(c):
      if graph[x][y]:
        move(x, y, graph[x][y], new_graph)
  graph = new_graph
print(ans)
