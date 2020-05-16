from collections import defaultdict

def solution(clothes):

    cloth_dict = defaultdict(list)
    total = 1

    for cloth in clothes:
        cloth_dict[cloth[1]].append(cloth[0])


    # 모든 경우의 수 : (의상 종류 별 개수 + 1) 를 종류 별로 모두 곱한 값
    # +1은 각 종류에서 안 입고 있는 경우까지 포함하기 위해
    for cloth in cloth_dict.keys() :
        total *= len(cloth_dict[cloth]) + 1

    # 문제에서 다 벗는 경우는 없다고 했으니 빼줌
    total -= 1

    return total

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face'],['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
