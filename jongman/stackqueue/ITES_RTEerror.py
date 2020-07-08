import sys

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

    i = 0
    nums = []
    q = num_generator(N)
    while i < N:
        nums.append(next(q))
        i += 1

    # print(nums)
    lo, hi = 0, 0
    total = 0
    cnt = 0

    while hi < len(nums) :
        # print(lo,hi)
        # print(total)
        if total == K :
            total += nums[hi]
            # print(nums[lo:hi])
            hi += 1
            cnt += 1

        elif total < K :
            total += nums[hi]
            hi += 1

        else :
            total -= nums[lo]
            lo += 1

    for i in range(lo, len(nums)) :
        total -= nums[lo]
        if total == K :
            print(nums[lo:len(nums)])
            cnt += 1

    print(cnt)