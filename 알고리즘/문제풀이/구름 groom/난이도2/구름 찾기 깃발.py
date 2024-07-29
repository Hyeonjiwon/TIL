import sys

# 상 i-1
# 하 i+1
# 좌 j-1
# 우 j+1
# 1 대각선 i-1, j+1
# 2 대각선 i-1, j-1
# 3 대각선 i+1, j-1
# 4 대각선 i+1, j+1

# x, y가 1이 아니면 구름이 아닌거임
# 구름이 아니면


def solution():
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, 1, -1, -1, 1]
    answer = 0

    # 구름인 좌표 주위 탐색
    for x, y in flag:
        for i in range(len(dx)):
            if board[x][y] == 1:
                nx = x + dx[i]
                ny = y + dy[i]

                # 격자 범위 안에서 구름이 아니면 -1
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                    board[nx][ny] -= 1

    # k인 수 찾기
    for x in range(n):
        for y in range(n):
            if board[x][y] == -k:
                answer += 1

    print(answer)


n, k = map(int, sys.stdin.readline().split())

board = [[] for _ in range(n)]
flag = []
for i in range(n):
    board[i] = list(map(int, sys.stdin.readline().split()))

    for j in range(n):
        if board[i][j] == 1:
            flag.append((i, j))

solution()
