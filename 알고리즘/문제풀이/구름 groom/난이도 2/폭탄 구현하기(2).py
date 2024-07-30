import sys

N, K = map(int, sys.stdin.readline().split())

ground1 = [[0] for _ in range(N)]
ground2 = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    ground1[i] = list(map(str, sys.stdin.readline().split()))

flag = []
for i in range(K):
    r, c = map(int, sys.stdin.readline().split())
    flag.append((r-1, c-1))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

m1 = 0
for x, y in flag:
    m2 = 0
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if ground1[nx][ny] == "0":
                ground2[nx][ny] += 1
            elif ground1[nx][ny] == "@":
                ground2[nx][ny] += 2
            m2 = max(m2, ground2[nx][ny])

    m1 = max(m1, m2)

print(m1)
