import heapq
import sys

T = int(sys.stdin.readline().rstrip())

def input_generator(n,a,b) :

    yield 1983
    prev= 1983
    for _ in range(n-1) :
        now = (prev * a + b) % 20090711
        yield now
        prev = now

for _ in range(T) :

    N, a, b = map(int, sys.stdin.readline().rstrip().split(" "))


    minHeap = []
    minSize = 0
    maxHeap = []
    maxSize = 0
    inputs = input_generator(N,a,b)
    medians = []
    for _ in range(N) :

        num = next(inputs)

        if minSize == maxSize :
            heapq.heappush(maxHeap, -num)
            maxSize += 1
        else :
            heapq.heappush(minHeap, num)
            minSize += 1

        if minHeap and maxHeap :
            minTop = abs(minHeap[0])
            maxTop = abs(maxHeap[0])

            if minTop < maxTop :
                maxTop = -heapq.heappop(maxHeap)
                minTop = -heapq.heappop(minHeap)

                heapq.heappush(maxHeap, minTop)
                heapq.heappush(minHeap, maxTop)

        medians.append(-maxHeap[0] % 20090711)

    print(sum(medians) % 20090711)

