# 백준 2875 대회 or 인턴

import sys

# N개
W, M, K = map(int, sys.stdin.readline().rstrip().split(" "))

team_cnt = 0
remain = team_cnt % 2
W -= remain

if W <= M*2 :
    # 여자 수/2가 팀 수
    team_cnt = W//2

else :
    # 남자 수가 팀 수
    team_cnt = M


remain = remain + (W - team_cnt*2) + (M - team_cnt)

diff = K-remain

if diff > 0 :

    team_cnt -= diff//3

    if (diff) % 3 != 0:
        team_cnt -= 1

print(team_cnt)


# 만들 수 있는 팀을 모두 만들고, K 만큼 팀을 못이룬 사람과 만든 팀에서 빼려고 한다.
# 경우를 둘로 나누었다.
# 여자 수가 남자 수의 두배보다 적거나 같으면 여자의 수를 2로 나눈 값이 팀의 개수가 된다.
# 여자 수가 남자 수의 두배보다 많으면 남자의 수가 팀의 수가 된다.
# 이때 여자의 수가 홀수라면 한명은 무조건 팀을 못이루니 미리 뺴놓아 계산을 쉽게 했다.
# (빼놓지 않으면 W=81, M=41인 경우에 조건문에 충족하지 않는다)
# 그렇게 팀의 개수와 팀을 못이룬 사람의 수를 계산해낸 뒤 K만큼 인원을 빼줬다.
# 팀을 못이룬 사람의 수가 K보다 크거나 같으면 그 사람들이 인턴을 가도 되니 팀의 수에는 변화가 없다.
# 만약 K가 더 크다면 팀으 하나씩 분해한다. 이때 K=4,5 라도 3명인 팀에서 한명이 빠지면 팀이 분해되기에 이를 처리하는 코드도 추가해야한다.
