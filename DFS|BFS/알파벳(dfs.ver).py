import sys
input = sys.stdin.readline
r, c = map(int, input().split())
graph = [list(map(lambda x: ord(x)-65, input().strip())) for _ in range(r)]
visited = [0] * 26
visited[graph[0][0]] = 1
step = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cur_step):
  global step
  step = max(cur_step, step)

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if (0 <= nx < r) and (0 <= ny < c) and visited[graph[nx][ny]] == 0:
      visited[graph[nx][ny]] = 1
      dfs(nx, ny, cur_step+1)
      visited[graph[nx][ny]] = 0
dfs(0,0, step)
print(step)
