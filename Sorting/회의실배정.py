import sys
input = sys.stdin.readline

meetings = int(input())
time = [list(map(int, input().split())) for _ in range(meetings)]
time.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end = time[0][1]
for i in range(1, meetings):
  if time[i][0] >= end:
    cnt += 1
    end = time[i][1]

print(cnt)
