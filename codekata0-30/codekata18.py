def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    while len(trucks_on_bridge):
        answer += 1
        trucks_on_bridge.pop(0)
        
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))   
            else:
                trucks_on_bridge.append(0)
        print(trucks_on_bridge, answer)
    return answer
        
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

a = solution(bridge_length, weight, truck_weights)
print(a)
#2	    10	    [7,4,5,6]	                        8
#100	100	    [10]                                101
#100	100	    [10,10,10,10,10,10,10,10,10,10]	    110