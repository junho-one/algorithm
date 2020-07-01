# 종만북 문제

import sys

# 1개
T = int(sys.stdin.readline().rstrip())

def findBig(left, right) :

    if left == right :
        return fences[left]

    mid = (left+right)//2

    leftArea = findBig(left,mid)
    rightArea = findBig(mid+1,right)

    lo = mid
    hi = mid+1

    minHeight = min(fences[lo], fences[hi])
    maxArea = minHeight * 2

    while left < lo or hi < right :

        if hi < right and (lo == left or (fences[hi+1] > fences[lo-1])) :
            hi += 1
            minHeight = min(minHeight, fences[hi])

        else :
            lo -= 1
            minHeight = min(minHeight, fences[lo])

        maxArea = max(maxArea, minHeight *(hi-lo+1))

    return max(maxArea, leftArea, rightArea)

for _ in range(T) :
    N = int(sys.stdin.readline().rstrip())
    fences = list(map(int,sys.stdin.readline().rstrip().split()))

    # print(fences)

    print(findBig(0,N-1))


# 1
# 7
# 7 1 5 9 6 7 3