# import sys
#
# T = int(sys.stdin.readline().rstrip())
#
# for _ in range(T) :
#
#     N = int(sys.stdin.readline().rstrip())
#     fences = list(map(int, sys.stdin.readline().rstrip().split()))
#     fences.append(0)
#     stack = []
#
#     maxSize = 0
#     for idx, height in enumerate(fences) :
#
#         while stack and stack[-1][1] > height :
#             nowidx, nowHeight = stack.pop()
#
#             if stack :
#                 width = idx - stack[-1][0] - 1 # stack의 맨 위에 있는 블록은 nowHeight의 왼쪽에 있는 블록중 처음으로 nowHeight보다 작은 블록을 의미
#             else :
#                 width = idx # 스택이 비어있다는 의미는 nowHeight가 현재 height이 나오기 이전까지 가장 작은 높이였다는 의미다.
#                             # 그러니까 nowHeight는 이떄까지 나온 블록에 모두 포함되어짐 => ( nowHeight * 이떄까지 나온 블록 수 )
#             maxSize = max(maxSize, width * nowHeight)
#
#         stack.append((idx,height))
#
#     print(maxSize)


import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T) :

    N = int(sys.stdin.readline().rstrip())
    fences = list(map(int, sys.stdin.readline().rstrip().split()))
    fences.append(0)
    stack = []

    area = 0
    prev = 0
    for idx, val in enumerate(fences) :

        if prev <= val :
            stack.append([idx,val])

        else :
            while stack and stack[-1][1] > val :
                _, top_val = stack.pop()

                if stack :
                    left = stack[-1][0]
                else :
                    left = -1

                area = max(area, top_val * (idx-left-1))

            stack.append([idx,val])
        prev = val

    print(area)


# 이전 값보다 큰거나 같은 값들은 모두 쌓고,
# 이전 값보다 작은 값이 나오면, while문을 통해 현재 값 보다 큰 이전 값들을 최대 높이로 가지는 넓이를 모두 구한다.

# 처음에는 현재 인덱스에서 pop을 통해 나오는 인덱스까지를 밑변으로 보고 구했는데,
# 2 4 3 4 5 6 3 4 같은 경우에서 에러가 난다. 즉, 자신까지가 아니라 그 뒤에 있는 인덱스까지 (현재 pop에서 나온 높이보다 최초로 작은 높이를 가지는 index)를 밑벼으로 해야 한다.

