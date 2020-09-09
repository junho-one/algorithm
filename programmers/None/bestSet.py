# 프로그래머스 최고의 집합
def solution(n, s):
    if n == 1:
        return [s]

    if s < n:
        return [-1]

    answer = []
    while n > 0:
        val = s // n
        rem = s % n

        if rem != 0:
            val += 1

        answer.append(val)
        s -= val
        n -= 1

    answer.sort()

    return answer

# 규칙을 찾아보면 현재 수에 n으로 나눈 값 (만약 나머지가 있으면 +1)
# 이 값은 최대 곱을 만드는 원소가 된다.
# 이 규칙을 반복해서 n이 0이 될 때까지 구하면 된다.

# 가장 큰 수가 되려면 s를 n으로 나눈 값의 언저리에 있는 값들로 구성되어야 한다는 점에서 착안