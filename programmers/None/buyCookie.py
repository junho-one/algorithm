def solution(cookie):
    answer = -1

    length = len(cookie)


    for i in range(length-1) :
        left_idx = i
        right_idx = i+1
        left_sum = cookie[left_idx]
        right_sum = cookie[right_idx]
        while left_idx < length:

            if right_idx == length-1 and left_sum > right_sum:
                break

            if left_sum > right_sum:
                right_idx += 1
                right_sum += cookie[right_idx]
                continue

            if left_sum <= right_sum:

                if left_sum == right_sum:
                    answer = max(answer, left_sum)

                left_idx += 1
                left_sum += cookie[left_idx]
                right_sum -= cookie[left_idx]
                continue

    return answer

print(solution([1,1,2,3]))
print(solution([1,2,4,5]))

# 쿠키의 길이가 2000으로 크지 않다.
# 첫째가 사는 바구니의 오른쪽 끝을 left_idx로 가리키고, 둘째가 사는 바구니의 끝을 right_idx가 가리킨다.
# 그리고 첫째의 과자 합을 left_sum, 둘째의 과자 합을 right_sum이라고 둔 후, 두 값을 비교하면서 left_idx와 right_idx를 움직인다.
# left_sum이 right_sum보다 크다면 right_idx를 움직여 right_sum 값을 더 키워야 하고,
# right_sum이 더 크다면 left_idx를 움직여 left_sum의 값을 키운다.

# 위 로직에서는 첫번째 인덱스가 고정이 된 상태로 가정하기에, for문으로 cookie length만큼 돌리며 시작 인덱스를 바꿔가면서 테스트한다.
