# 백준 검열, 3111번
# 시간초과. 너무 어렵네

import sys
from collections import deque

# 1개
A = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()
A = list(A)
reverse_A = list(reversed(A))
len_A = len(A)

front = []
back = []

frontIdx = 0
backIdx = len(T)-1

flag = True

while frontIdx <= backIdx :

    if flag :
        front.append(T[frontIdx])
        frontIdx += 1
        if front[-len_A:] == A :
            # front = front[:-len_A]
            front[-len_A:] = []
            # 위 두 명령어의 시간 차이는 엄청나다.
            # 밑에 있는 명령어는 len_A만큼 걸리는거 같은데
            # 위에 있는 명령어는 아마 front-len_A 만큼 걸리기에 front가 커지면 엄청난 시간이 걸리는 듯듯
            flag = False

    else :
        back.append(T[backIdx])
        backIdx -= 1

        if back[-len_A:] == reverse_A:
            # back = back[:-len_A]
            back[-len_A:] = []
            flag = True

# A+B하는 순간
# 여기서 새로운 A가 만들어질 수도 있다.  front : aaaaaaa,  back : bbbbbbb 인데 ab를 찾는

while back :
    front.append(back.pop())

    if front[-len_A:] == A:
        # front = front[:-len_A]
        front[-len_A:] = []

answer = "".join(front)
print(answer)



# 문자열 T의 맨 앞에서 전진해나가면서 문자열을 하나씩 채우는 front와 맨 뒤에서 앞으로 가면서 문자열을 채우는 back이 있다.
# 앞에서 부터 문자열을 찾을 때는 front에 문자열을 하나씩 넣고 매번 front에 쌓인 문자열이 A와 같은지 비교한다
# 만약 A와 같다면 그 부분을 stack에서 빼내고 다시 새문자열을 받아 쌓는다.
# B도 방향만 다를 뿐 위와 같은 방식으로 움직인다. 값을 채우기 위해 frontIdx와 backIdx를 사용하면 쉽게 구현할 수 있다.

# 그러다 frontIdx가 backIdx가 같아지는 순간 더이상 반대편 부분은 겁사할 필요가 없으니 front와 back을 합친다.
# 하지만 이때 front와 back이 합쳐지면 A가 생기는 경우가 있다
# 예를들어 A = ab이고, front = [a,a,a,a], back = [b,b,b,b]라면 front+back을 하면 ab가 생겨난다.
# 이런 경우를 대비해 back에 있는 문자열을 front에 넣어주면서 두 리스트가 합쳐졌을 때 생기는 문자열 A를 모두 제거해준다.

