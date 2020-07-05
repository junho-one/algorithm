# 백준 10610, 30
import sys

def relocate(num_list) :

    num_list = sorted(num_list, reverse=True)

    return ''.join( str(s) for s in num_list)

# 1개
number = list(map(int, sys.stdin.readline().rstrip()))

if 0 in number and sum(number) % 3 == 0:
    print(relocate(number))

else :
    print(-1)

# 숫자가 3의 배수가 되려면 모든 수의 합이 3의 배수여야 한다.
# 그런데 30의 배수니 0이 무조건 하나는 들어가야 1의 자리가 0이되서 30의 배수를 만족한다.
# 이 두 조건을 만족하고 가장 큰수부터 뽑으면 최대 숫자가 된다
