def solution(bridge_length, weight, truck_weights):
    time = 1
    cap = 0
    t_out = []
    t_in = [(truck,0) for truck in truck_weights]
    bridge = []
    while truck_weights != t_out:
        if t_in and cap + list(t_in[0])[0] <= weight:
            truck = t_in.pop(0)
            bridge.append(truck)
            key,val = truck
            cap += key
        time += 1
        for ind, tup in enumerate(bridge):
            tup = list(tup)
            tup[1] += 1
            bridge[ind] = tuple(tup)
        key, val = bridge[0]
        if val >= bridge_length:
            bridge.pop(0)
            cap -= key
            t_out.append(key)
    return time

# or

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    while bridge:
        bridge.pop(0)
        time += 1
        if truck_weights:
            if sum(bridge)+truck_weights[0]<=weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return time
