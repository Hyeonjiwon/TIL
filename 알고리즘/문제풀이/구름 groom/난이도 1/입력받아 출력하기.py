import sys

N = int(sys.stdin.readline())
A, B = sys.stdin.readline().split()


for i in range(1, N+1):
    line = ""
    for j in range(1, N+1):
        if (i*j) % 2 == 0:
            line += B + " "
        else:
            line += A + " "
    print(line)
