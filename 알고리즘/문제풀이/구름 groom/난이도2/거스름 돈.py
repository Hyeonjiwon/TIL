import sys
import math

N = int(sys.stdin.readline())

# 그리디
coins = [40, 20, 10, 5, 1]
cnt = 0
for i in range(len(coins)):
    cnt += N // coins[i]
    N = N % coins[i]

print(cnt)
