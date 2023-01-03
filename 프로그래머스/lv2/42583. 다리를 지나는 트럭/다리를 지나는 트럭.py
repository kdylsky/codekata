def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length
    total = 0
    while q:
        k = q.pop(0)
        total-=k
        time += 1
        if truck_weights:
            if total + truck_weights[0] <= weight:
                pop_truck = truck_weights.pop(0)
                total+=pop_truck
                q.append(pop_truck)
            else:
                q.append(0)
    return time