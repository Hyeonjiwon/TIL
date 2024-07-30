import sys
import math

N = int(sys.stdin.readline())
items = [14, 7, 1]

cnt = 0
for i in range(len(items)):
    cnt += N // items[i]
    N = N % items[i]

print(cnt)
