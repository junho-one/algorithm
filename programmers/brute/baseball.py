def solution(baseball):
    answer = 0

    allcase = list( map(str, list(range(100,1000))) )
    notIdxs = []
    for i in range(len(allcase)-1,-1,-1) :
        if '0' in allcase[i] :
            notIdxs.append(i)
        elif len(set(allcase[i])) != 3 :
            notIdxs.append(i)

    for idx in notIdxs :
        allcase.pop(idx)

    for ques in baseball :

        num, strk, ball = ques

        if strk + ball == 3 :
            
        elif strk + ball == 2:

        elif strk + ball == 1:

        else :





    return answer


solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])