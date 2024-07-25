import sys

n, m = map(int, sys.stdin.readline().split())

total_c = 0 
for _ in range(n):
	c, v = map(int, sys.stdin.readline().split())
	total_c += c * v

if total_c <= m:
	print(m - total_c)
else:
	print("No")