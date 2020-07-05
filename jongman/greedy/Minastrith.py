import sys

# 1개
T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    N = int(sys.stdin.readline().rstrip())
    R = 8
    check_points = []

    for _ in range(N) :
        y, x, r = map(int, sys.stdin.readline().rstrip().split(" "))
        check_points.append((y,x,r))

