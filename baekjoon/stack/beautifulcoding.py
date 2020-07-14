# 백준 코딩은 예쁘게, 2879
import sys

def calCount( differences ) :

    if not differences :
        return 0

    if len(differences) == 1 :
        return differences[0]

    minVal = min(differences)
    minIdx = differences.index(minVal)

    cnt = minVal
    # 최소값으로 찢어진 양쪽 리스트는 찢어지기 이전에 모두 최소값 만큼은 같이 작업을 수행할 수 있으므로 최소값만큼 빼줘야 한다.
    # 리스트를 모두 돌면서 원소들을 빼주기에는 시간이 오래걸리므로 아래와 같이 하면 된다.
    # 이때 빈 리스트에서는 0을 반환하는데 cnt가 음수가 될 수는 없으니까 처리해줘야 한다.
    cnt += max(0, calCount(differences[:minIdx]) - minVal)
    cnt += max(0, calCount(differences[minIdx+1:]) - minVal)

    return cnt

# 1개
N = int(sys.stdin.readline().rstrip())

now = list(map(int,sys.stdin.readline().rstrip().split()))
right = list(map(int,sys.stdin.readline().rstrip().split()))

difference = [ x1-x2 for x1,x2 in zip(now,right)]

prev_sign = difference[0] > 0
same = []
answer = 0

# sign : True == + , False == -
for idx, diff in enumerate(difference) :

    now_sign = diff > 0

    if prev_sign == now_sign :
        same.append(abs(diff))

    else :
        answer += calCount(same)
        same = []
        same.append(abs(diff))
        prev_sign = now_sign

answer += calCount(same)

print(answer)


# 같은 작업을 해야하는 줄을 최대한 많이 모아서 분할정복으로 푼다.
# 현재 인텐트 - 올바른 인텐트를 하면 각 줄마다 어떤 작업을 해야하는지 알 수 있다.

# 반복문을 통해 첫번째 줄부터 끝까지 탐색해나간다.
# 현재 줄에서 해야하는 작업이 이전 줄에서 해야하는 작업과 같은 작업이라면 same이라는 리스트에 넣어서 보관해둔다.
# 만약 다른 작업이라면 현재 줄과 이전 줄들은 작업을 같이 수행할 수 없기에 이전 줄까지 모아둔 작업들을 처리한다.

# 모아둔 작업들을 담고있는 리스트 X가 수행해야하는 최소 횟수를 계산한다.
# 이 작업을 처리할 때는 리스트에서 최소값을 찾고 그 위치를 기준으로 왼쪽 부분 리스트와 오른쪽 부분 리스트로 나눌 수 있다.
# 나눠진 왼쪽, 오른쪽 리스트는 갖고 있는 값에서 방금 찾은 최소값 만큼은 처리하고 남은 처리 횟수가 들어있는 리스트들이다.
# 이를 분할해 나가면서 처리하면 리스트 X의 최소 수행횟수가 나온다.
