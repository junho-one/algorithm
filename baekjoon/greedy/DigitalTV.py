import sys

# 1개
N = int(sys.stdin.readline().rstrip())

Channels = []

for _ in range(N) :
    Channels.append(sys.stdin.readline().rstrip())


idx_k1 = Channels.index('KBS1')
idx_k2 = Channels.index('KBS2')

first = min(idx_k1, idx_k2)
second = max(idx_k1, idx_k2)

answer =  "1"*first + "4"*first + "1"*second + "4"*(second-1)

if Channels[second] == 'KBS1' :
    answer += '4'

print(answer)

# 설명 x
