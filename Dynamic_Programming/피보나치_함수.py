import sys
input = sys.stdin.readline

call0 = [1, 0]
call1 = [0, 1]
for i in range(2, 41):
  call0.append(call0[i-1]+call0[i-2])
  call1.append(call1[i-1]+call1[i-2])

t = int(input())
for _ in range(t):
    n = int(input())
    print(call0[n], call1[n])
