import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def action(color, location):
    if not buttons:
        return location

    # 만약 그 다음 버튼이 내꺼라면
    if color == buttons[0]:
        # 내가 그 위치에 있다면 버튼 누르기
        if location == int(buttons[1]):
            print(color, "click")
            return "click"
        # 아니라면 버튼 쪽으로 한칸 이동하기
        else:
            print(color, "move")
            # 오른쪽으로 갈지 왼쪽으로 갈지 결정
            direction = 1 if location < int(buttons[1]) else -1
            # 이동
            location += direction
        return location

    # 만약 다음버튼이 내꺼가 아니라면
    else:
        # 내가 가야할 다음 버튼을 찾고
        try:
            target = int(buttons[buttons.index(color) + 1])
        except:
            # 없으면 내가 눌러야 될 버튼이 없기 때문에 종료
            return location

        # 내가 그 버튼위치에 없다면 그 버튼쪽으로 한칸 이동
        if location != target:
            print(color, "move")
            direction = 1 if location < target else -1
            location += direction
        return location

for tc in range(1, T+1):
    buttons = input().split()
    num = buttons.pop(0)
    
    # 둘 다 1번 칸, 오른쪽방향으로 시작
    b = o = 1
    N = 0

    # 누를 버튼이 남아 있을 동안 이동
    while buttons:
        N += 1
        # 일단 b가 먼저 이동
        temp_b = action('B', b)

        # b가 버튼을 클릭했을때 같은 턴에 o가 클릭하면 안되기 때문에
        if temp_b == "click":
            # o가 움직이고 나서 b가 클릭한 버튼 제거
            o = action('O', o)
            buttons.pop(0)
            buttons.pop(0)
        # b가 이동 또는 아무것도 하지 않았을때
        else:
            b = temp_b
            # o가 버튼 클릭 후 제거
            temp_o = action('O', o)
            if temp_o == "click":
                buttons.pop(0)
                buttons.pop(0)
            # o가 이동 또는 아무것도 하지 않음
            else:
                o = temp_o
    print("#%d %d" % (tc, N))













    # # 가야 하는 위치에 먼저 갈 수 있도록 본인 리스트 만들어 놓기
    # b_buttons = []
    # o_buttons = []  

    # # 리스트 순회하면서 데이터 가공해서 넣기
    # for i in range(num):
    #     if arr[i*2] == "B":
    #         b_buttons.append(arr[i*2+1])
    #     else:
    #         o_buttons.append(arr[i*2+1])