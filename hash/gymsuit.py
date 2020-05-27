def solution(n, lost, reserve):
    answer = 0

    setlost = set(lost)
    setreserve = set(reserve)

    lost = list(setlost - setreserve)
    reserve = list(setreserve - setlost)


    reserve = sorted(reserve)
    lost = sorted(lost)

    # set과 dictionary는 값의 개수가 적으면 해시 충돌이 드물어 O(1) 이라 in으로 해결
    for r_p in reserve :

        if r_p-1 in lost :
            lost.remove(r_p-1)

        elif r_p+1 in lost :
            lost.remove(r_p+1)

    answer = n - len(lost)

    return answer


print(solution(3,[3],[1]))