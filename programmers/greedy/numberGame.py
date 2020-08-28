# 프로그래머스 숫자게임

def solution(A, B):
    answer = 0

    A = sorted(A)
    B = sorted(B)

    b_idx = 0
    for a in A:

        while b_idx < len(B) and B[b_idx] <= a:
            b_idx += 1

        if b_idx == len(B):
            break

        answer += 1
        b_idx += 1

    return answer