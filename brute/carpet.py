def solution(brown, yellow):
    answer = []

    yellows = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            if i >= yellow//i :
                yellows.append((i, yellow//i))

    for width, height in yellows :

        sums = (width+2)*2 + height*2

        if sums == brown :
            return [width+2,height+2]
    return 0

print(solution(10,2))