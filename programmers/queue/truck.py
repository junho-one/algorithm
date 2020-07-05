def solution(bridge_length, weight, truck_weights):

    bridge = []
    count = 0
    time = 0
    timer = []

    # timer : 트럭이 다리 위에서 얼마만큼의 시간을 보냈는지를 나타냄
    # bridge : 다리 위에 있는 트럭들을 나타

    # truck index를 가르키는 count
    while count < len(truck_weights) :

        time += 1

        # 만약 timer에 값이 있다면 -1을 해준다.
        timer = [x - 1 for x in timer]
        # timer의 맨 앞 값이 0이 되면 트럭이 맨 끝에 도착했다는 의미다. 맨 앞에있는 트럭을 뺴준다.
        if timer and timer[0] == 0:
            timer.pop(0)
            bridge.pop(0)

        bridge_weight = sum(bridge)

        # 현재 대기하는 트럭이 다리 위에 올라가도 weight를 넘지 않는다면 트럭을 추가한다.
        if truck_weights[count] + bridge_weight <= weight :
            bridge.append(truck_weights[count])
            count += 1
            timer.append(bridge_length)

    # while문이 끝났는데 timer에 값이 남아 있으면 아직 트럭이 다리 위에 있다는 의미
    # timer의 값이 다리를 지날 때 까지 남은 시간을 의미하니까 가장 최근 들어온 트럭의 값을 더해준다.
    if timer :
        time += timer[-1]

    return time




print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))
print(solution(100,100,[10]))