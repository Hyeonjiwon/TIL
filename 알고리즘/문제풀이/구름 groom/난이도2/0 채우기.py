import sys

N = int(sys.stdin.readline())
board = [[] for _ in range(N)]
flag = []

for i in range(N):
    board[i] = list(map(int, sys.stdin.readline().split()))

    for j in range(N):
        if board[i][j] == 0:
            flag.append((i, j))

ans = 0
for x, y in flag:
    for i in range(N):
        ans += board[x][i]
        ans += board[i][y]

print(ans)
