import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

def num_generator(count) :

    prev = 1983
    i = 0
    yield prev

    while i < count:
        prev = (prev * 214013 + 2531011) % pow(2, 32)
        show = prev % 10000 + 1
        i += 1
        yield show


for _ in range(T) :
    K, N = map(int, sys.stdin.readline().rstrip().split(" "))

    generator = num_generator(N)

    total = 0
    queue = deque()
    cnt = 0

    for i in range(N) :

        now = next(generator)
        queue.append(now)
        total += now

        if total == K :
            cnt += 1

        if total > K :
            while total > K :
                prev = queue.popleft()
                total -= prev
                if total == K :
                    cnt += 1
    print(cnt)
