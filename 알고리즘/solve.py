# 인프런 알고리즘 문제풀이 - 1. 재귀함수(스택프레임)
import sys

def recursive(n):
    if n == 0: return # 함수 종료
    else:
        # print(n)
        recursive(n-1)
        print(n, sep=' ')

n = int(sys.stdin.readline())
recursive(n)