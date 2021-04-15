import sys
input = sys.stdin.readline

def turn(n, d):
    if d == -1: # 반시계
        wheels[n] = wheels[n][1:] + wheels[n][:1]
    else: # 시계
        wheels[n] = wheels[n][-1:] + wheels[n][:-1]

def turn_nei(n, d, nei):
    if not 0 <= nei <= 3: return
    if n < nei and wheels[n][2] != wheels[nei][6]:
        turn_nei(nei, -d, nei + 1)
        turn(nei, d)
    elif n > nei and wheels[n][6] != wheels[nei][2]:
        turn_nei(nei, -d, nei - 1)
        turn(nei, d)


wheels = [list(map(int, input().rstrip())) for _ in range(4)]
ans = 0

for _ in range(int(input())):
    n, d = map(int, input().split())
    n -= 1

    turn_nei(n, -d, n + 1)
    turn_nei(n, -d, n - 1)
    turn(n, d)

for i in range(4):
    if wheels[i][0]: ans += pow(2, i)

print(ans)
