import sys

t = int(sys.stdin.readline())

for _ in range(t):
	x, y, n = map(int, sys.stdin.readline().split())
	
	# 1, 2 거리 1 + 2 = 3
	# 3초 6초 9초 가능 
	# total은 n 이하여야 경로까지 이동 가능
	# 거리와 시간을 뺏을때 짝수면 도착, 홀수면 도착할 수 있는 방법 없음
	total = abs(x) + abs(y)
	
	answer = "NO"
	if(total <= n and (total - n) % 2 == 0): 
		answer = "YES"
	
	print(answer)