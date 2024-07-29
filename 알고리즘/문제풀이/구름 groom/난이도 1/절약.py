import sys

n = int(sys.stdin.readline())

in_v = 0
out_v = 0

for _ in range(n):
    c, v = sys.stdin.readline().split()

    if c == "in":
        in_v += int(v)
    else:
        out_v += int(v)

    if in_v < out_v:
        print("fail")
        break

if in_v >= out_v:
    print("success")
