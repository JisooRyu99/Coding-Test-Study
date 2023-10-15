# https://school.programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    truck_sum = 0
    
    while bridge:
        truck_sum -= bridge[0]
        bridge.pop(0)
        answer+=1
        
        if truck_weights:
            if truck_sum + truck_weights[0] <= weight:
                truck_sum += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
        
    return answer



############################# 시간 초과 #############################
'''
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    
    while bridge:
        bridge.pop(0)
        answer+=1
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
        
    return answer
'''