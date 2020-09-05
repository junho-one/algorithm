from math import sqrt


def solution(begin, end):
    result = []
    if begin == 1:
        result.append(0)
        begin += 1
    for i in range(begin, end + 1):
        for j in range(2, int(sqrt(end) + 1)):
            # 소수가 아니라면 가장 작은 약수로 나눈 값. + 10000000 블록이 끝이기에.
            if i % j == 0 and i // j < 10000000:
                result.append(i // j)
                break
        # 소수라면 1
        else:
            result.append(1)
    return result

# # 핵심은 소수를 찾는 것.
# # 만약 소수라면 1과 자가자신 이외에는 어떤 수로도 나눠지지 않는다.
# # 소수 판별에서 가장 효율적인 방법은 2~해당숫자 루트값까지 순화하며 % == 0이 되는지 확인