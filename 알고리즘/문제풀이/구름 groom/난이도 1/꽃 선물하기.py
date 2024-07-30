import sys

N = int(sys.stdin.readline())

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())

    if a < b:
        print("Sunflower")
    elif a == b:
        print("Tulip")
    else:
        print("Rose")
