def solution(bridge_length, weight, truck_weights):
    queue = {1:truck_weights.pop(0)}
    print(queue)
    answer = 1
    # while truck_weights:
        for k, v in queue.items():
            queue[k+1] = v

        queue.pop(bridge_length+1)
        print(queue)
        total_weight = sum(queue.values())
        print(total_weight)
        if total_weight + truck_weights[0] <= weight:
            queue[truck_weights.pop(0)] = 1
            print(queue)
    answer += 1
    return answer