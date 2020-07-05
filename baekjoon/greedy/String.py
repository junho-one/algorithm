# 백준 1120 문자열

import sys

A, B = map(list,sys.stdin.readline().rstrip().split(" "))

len_diff = len(B) - len(A)

def diffOfStr(A,B) :
    diff = 0
    for i in range(len(A)) :
        if A[i] != B[i] :
            diff += 1
    return diff

diff_list = []

for i in range(len_diff+1) :
    sub_B = B[i:i+len(A)]

    diff_list.append(diffOfStr(A,sub_B))

left_cnt = diff_list.index(min(diff_list))

print(diff_list)
print(min(diff_list))

# 앞 뒤로 넣을 때 각 위치에 맞는 글자를 넣으니 문자열 간의 차이가 늘어날리는 없다.
# 그러니 현재 A를 B의 어느 위치에 매칭시켜야하는지만 결정하면 된다.
# B의 크기가 A의 크기랑 같아지게 슬라이싱을 한다. 그리고 두 문자열간의 차이를 구하고 이 값이 최소가 되는게
# B에 문자열을 추가했을 때 문자열간의 최소값이 된다.

# adaabc aababbcd가 주어졌을 때 adaabc가 위치할 수 있는 자리는 총 3가지다.
# 1. adaabc,aababb 2. adaabc,ababbc 3. adaabc,babbcd
# 이때 각각의 문자열 차이는 3, 2, 6이 나온다.
# 어차피 지금부터 추가될 문자는 잘 넣으면 A와 문자열 차이가 늘어나지 않는다.
# 그렇기에 차이가 발생하는 지점은 바꿀 수 없는 문자열인 A에서만 나온다. 이 지점을 최소화한 값이 전체 값의 최소가 된다.

