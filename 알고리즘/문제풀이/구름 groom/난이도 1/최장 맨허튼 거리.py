import sys

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

x = abs(arr[2]-arr[0])
y = abs(arr[3]-arr[1])

print(x+y)
