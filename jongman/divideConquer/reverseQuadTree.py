# 종만북 문제

import sys

N = int(sys.stdin.readline().rstrip())


def reverse() :
    global it

    head = string[it]
    it += 1

    if head == 'b' or head == 'w' :
        return head

    upperLeft = reverse()
    upperRight = reverse()
    lowerLeft = reverse()
    lowerRight = reverse()

    return "x" + lowerLeft + lowerRight + upperLeft + upperRight

for _ in range(N) :

    string = sys.stdin.readline().rstrip()
    it = 0
    print( reverse() )