import collections

def solution(priorities, location):
    priorities = collections.deque(priorities)
    #내 문서가 출력될 순서
    order = 0
    
    while True:
        first_queue = priorities[0]
        mx = max(priorities)
        
        # 만약 내 문서가 제일 앞에 있는 문서이고
        if location == 0:
            # 중요도가 제일 높다면 프린트 후 order return
            if first_queue >= mx:
                order += 1
                return order
            # 중요도가 낮다면 list를 왼쪽으로 한칸씩 밀기
            else:
                priorities.rotate(-1)
                location = len(priorities) - 1
            
        else:
            if first_queue >= mx:
                priorities.popleft()
                order += 1
                location -= 1
            else:
                priorities.rotate(-1)
                location -= 1