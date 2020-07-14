# 백준 검열, 3111번
# 시간초과. 너무 어렵네

import sys

# 1개
A = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()
reverse_A = A[::-1]
len_A = len(A)

front = ["2"] * len_A
back = ["2"] * len_A

frontIdx = 0
backIdx = len(T)-1

flag = True

while frontIdx <= backIdx :

    if flag :
        front.append(T[frontIdx])
        frontIdx += 1

        if "".join(front[-len_A:]) == A :
            front = front[:-len_A]
            flag = False

    else :
        back.append(T[backIdx])
        backIdx -= 1

        if "".join(back[-len_A:]) == reverse_A:
            back = back[:-len_A]
            flag = True

# A+B하는 순간
# 여기서 새로운 A가 만들어질 수도 있다.  front : aaaaaaa,  back : bbbbbbb 인데 ab를 찾는

while back :
    front.append(back.pop())

    if "".join(front[-len_A:]) == A:
        front = front[:-len_A]

front = front[len_A:]
front = front[:-len_A]

answer = "".join(front)
print(answer)



