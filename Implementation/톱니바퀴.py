import sys
input = sys.stdin.readline

def turn_nei(n, d, nei):
    if not 0 <= nei <= 3: return
    if n > nei and wheels[n][6] != wheels[nei][2]:
        turn_nei(nei, -d, nei - 1)
        turn(nei, d)
    elif n < nei and wheels[n][2] != wheels[nei][6]:
        turn_nei(nei, -d, nei + 1)
        turn(nei, d)

def turn(n ,d):
    if d == 1: wheels[n] = wheels[n][-1:] + wheels[n][:-1]
    else: wheels[n] = wheels[n][1:] + wheels[n][:1]

wheels = [list(map(int, input().rstrip())) for _ in range(4)]
for _ in range(int(input())):
    n, d = map(int, input().split())
    n -= 1
    turn_nei(n, -d, n + 1)
    turn_nei(n, -d, n - 1)
    turn(n, d)

print(sum(2 ** i if wheels[i][0] else 0 for i in range(4)))
