from collections import deque

def solution(bridge_length, weight_max, truck_before):
    truck_before, truck_now ,truck_after = deque(truck_before), deque([]), deque([])

    num_trucks = len(truck_before)
    answer, weight_now = 0, 0
    while len(truck_after) < num_trucks:
        answer += 1

        tmp = 0 if len(truck_before) == 0 else truck_before[0]
        if weight_now + tmp <= weight_max:
            weight_now += tmp
            if len(truck_before) > 0:
                truck_now.append(truck_before.popleft())
            else: truck_now.append(0)
        else:
            truck_now.append(0)

        if len(truck_now) == bridge_length:
            if truck_now[0] == 0:
                truck_now.popleft()
            else:
                weight_now -= truck_now[0]
                truck_after.append(truck_now.popleft())

    return answer + 1
