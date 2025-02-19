class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net_cost = [gas[i]-cost[i] for i in range(len(gas))]
        visited = [0] * len(net_cost)
        
        start_idx = 0
        while True:
            # 모든 경우의 수가 불가한 경우
            if start_idx >= len(gas):
                return -1

            # 한바퀴를 돌아 다시 방문했던곳을 방문한 경우
            if visited[start_idx]:
                return -1
            
            # 시작점부터 불가능한 경우
            if net_cost[start_idx] < 0:
                start_idx += 1
                continue
            
            visited[start_idx] = 1
            tank = 0
            for i in range(len(net_cost)):
                idx = (start_idx + i) % len(net_cost)
                tank += net_cost[idx]

                if tank < 0:
                    start_idx = idx+1
                    break
            else:
                return start_idx