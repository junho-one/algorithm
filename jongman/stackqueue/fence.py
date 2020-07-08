import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T) :

    N = int(sys.stdin.readline().rstrip())
    fences = list(map(int, sys.stdin.readline().rstrip().split()))
    fences.append(0)
    stack = []

    maxSize = 0
    for idx, height in enumerate(fences) :

        while stack and stack[-1][1] > height :
            nowidx, nowHeight = stack.pop()

            if stack :
                width = idx - stack[-1][0] - 1 # stack의 맨 위에 있는 블록은 nowHeight의 왼쪽에 있는 블록중 처음으로 nowHeight보다 작은 블록을 의미
            else :
                width = idx # 스택이 비어있다는 의미는 nowHeight가 현재 height이 나오기 이전까지 가장 작은 높이였다는 의미다.
                            # 그러니까 nowHeight는 이떄까지 나온 블록에 모두 포함되어짐 => ( nowHeight * 이떄까지 나온 블록 수 )
            maxSize = max(maxSize, width * nowHeight)

        stack.append((idx,height))

    print(maxSize)
