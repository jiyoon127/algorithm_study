# without using combinations ver(use backtracking)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(50000)

n = int(input())
member = [False] * n
abilities = []
start = []
link = []
min_diff = int(1e9)
synergy = []

for _ in range(n):
  abilities.append(list(map(int, input().split())))

def get_score(team, score):
  global s_score, l_score
  if len(synergy) == 2:
    if team == start:
      s_score += abilities[synergy[0]][synergy[1]]
    else:
      l_score += abilities[synergy[0]][synergy[1]]
    return
  for i in range(len(team)):
    if synergy and synergy[-1] == team[i]:
      continue
    synergy.append(team[i])
    get_score(team, score)
    synergy.pop()

def make_team():
  global min_diff, s_score, l_score
  if len(start) == n//2:
    link = [i for i in range(n) if i not in start]
    s_score = 0
    l_score = 0
    get_score(start, 0)
    get_score(link, 0)

    min_diff = min(min_diff, abs(s_score - l_score))
    return
  for i in range(n):
    if member[i]: continue
    member[i] = True
    start.append(i)
    make_team()
    start.pop()
    for j in range(i+1, n):
      member[j] = False

make_team()
print(min_diff)


##############################################################
# use combinations ver

from itertools import combinations
import sys
input = sys.stdin.readline
sys.setrecursionlimit(50000)

n = int(input())
member = [i for i in range(n)]
abilities = []
start = []
link = []
min_diff = int(1e9)

for _ in range(n):
  abilities.append(list(map(int, input().split())))

def get_score(team_a, team_b):
  global min_diff
  sum_a = 0
  sum_b = 0
  for i, j in list(combinations(team_a, 2)):
    sum_a += abilities[i][j] + abilities[j][i]
  for i, j in list(combinations(team_b, 2)):
    sum_b += abilities[i][j] + abilities[j][i]
  min_diff = min(min_diff, abs(sum_a - sum_b))

def team():
  for comb in combinations(member, n//2):
    start = list(comb)
    link = list(set(member) - set(start))
    get_score(start, link)

team()
print(min_diff)
