# 백준 외계인의 기타 연주, 2841번

import sys

# N개
N, P= map(int, sys.stdin.readline().rstrip().split(" "))

melody = []

stacks = [  [-1] for _ in range(7)]

for _ in range(N) :
    line, plat = map(int, sys.stdin.readline().rstrip().split(" "))
    melody.append((line, plat))

cnt = 0
for line, plat in melody :

    if plat > stacks[line][-1] :
        cnt += 1
        stacks[line].append(plat)

    elif plat < stacks[line][-1] :
        while stacks[line] and plat < stacks[line][-1] :
            stacks[line].pop()
            cnt += 1

        if  stacks[line][-1] != plat :
            cnt += 1
            stacks[line].append(plat)

print(cnt)


# stacks[i]에 -1을 넣은 이유는 항상 stacks[i][-1]을 체크할 때 스택이 이 비어있는지를 체크해야하는 번거로움이 있기 때문이다.
# plat은 항상 1보다 크기 때문에 -1 을 넣어두면 스택이 비어있는 경우는 존재하지 않게 된다.

# stacks[i]가 i번째 기타줄에서 누르고 있는 플랫 번호들을 담고 있다.
# 플랫을 3, 5, 7같이 오름차순으로 누를 때는 번호가 작은 것을 뗄 이유가 없으므로 같이 누른다.
# 만약 새로운 플랫이 들어오면 항상 번호가 큰것 부터 지워나가면 최소한의 떼는 수로 들어오는 플랫의 음을 낼 수 있다.
# stakcs[i]에서 누르고 있는 플랫 중 가장 높은 플랫 번호가 음을 내야하는 플랫 번호와 같다면 손가락을 데거나 떼는 행위를 하지 않아도 된다.

# 플랫와 기타번호를 순서대로 입력받으며 위와 같은 조건문을 작성해주면 문제가 해결된다.
# 시간복잡도는 입력을 순서대로 하나씩 받아오니 끝까지 처리한다면 O(N)
# while문이 발생하는 최대 횟수는 N이니
# O(N)이 될 것 같다.   <- 맞는지 모르겠다.



