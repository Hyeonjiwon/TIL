import sys
import math

T = int(sys.stdin.readline())

size = 0
for _ in range(T):
    w, h = map(int, sys.stdin.readline().split())
    size = max(size, w*h)

print(size)
