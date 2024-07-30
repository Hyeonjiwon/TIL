import sys

N, K = map(int, sys.stdin.readline().split())
S = sys.stdin.readline()

ans = ""
for i in range(N):
    ans += str(int(S[i]) + K)

print(ans)
