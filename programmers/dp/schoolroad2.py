# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys


def var(a, b):
    return (a * b) / ((a + b + 1) * (a + b) * (a + b))


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())

    feedbacks = []
    for _ in range(N):
        id, type, cnt = sys.stdin.readline().rstrip().split(" ")
        feedbacks.append((id, type, cnt))

    a = 1
    b = 15
    minS = var(a, b)
    maxS = var(a, b)

    for fb in feedbacks:
        if fb[1] == 'imp':
            b += int(fb[2])

        else:
            a += int(fb[2])
            b -= int(fb[2])

        Sk = var(a, b)
        if minS > Sk:
            minS = Sk

        if maxS < Sk:
            maxS = Sk

        print(Sk, minS, maxS)