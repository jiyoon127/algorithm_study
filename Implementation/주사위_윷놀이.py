import sys
input = sys.stdin.readline

dice = list(map(int, input().split()))
graph = [[i * 2 for i in range(21)]+[0]]
piece = [[0, 0] for _ in range(4)]
max_val = -int(1e9)

graph.append([10, 13, 16, 19, 25])
graph.append([20, 22, 24, 25])
graph.append([30, 28, 27, 26, 25])
graph.append([25, 30, 35, 40, 0])

def simulate(diceIdx, score):
  global max_val
  if diceIdx == 10: 
    max_val = max(max_val, score)
    return

  for i in range(4):
    x, y = piece[i][0], piece[i][1]

    if y == len(graph[x]) - 1: continue
    if diceIdx == 9 and score + 40 <= max_val: continue
    nx, ny = x, y + dice[diceIdx]
    if x == 0:
      if ny == 5: nx, ny = 1, 0
      elif ny == 10: nx, ny = 2, 0
      elif ny == 15: nx, ny = 3, 0
      elif ny == 20: nx, ny = 4, 3
      
    elif x < 4: 
      if ny >= len(graph[x]) - 1:
        nx = 4
        ny -= len(graph[x]) - 1
      
    if ny >= len(graph[nx]):
      ny = len(graph[nx]) - 1

    if graph[nx][ny] != 0 and [nx, ny] in piece:
      continue
    
    piece[i] = [nx, ny]
    score += graph[nx][ny]
    simulate(diceIdx + 1, score)
    piece[i] = [x, y]
    score -= graph[nx][ny]

simulate(0, 0)
print(max_val)
