# 못품
# [1,1,2,4] 가 있다면 이 수들의 합은 8이다.
# 그러면 8까지 모든 수를 조합으로 만들 수 있다고 한다..
def solution(weight):
    answer = 0

    weight = sorted(weight)

    cover = weight[0]
    for w in weight[1:] :
        if w <= cover + 1 :
            cover += w
        else :
            break
    return cover+1




solution([3, 1, 6, 2, 7, 30, 1])

