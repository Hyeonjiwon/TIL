import sys

n = int(sys.stdin.readline())

result = ""
while n > 0:
	result += str(n%2)
	n = n//2
	
print(result[::-1])