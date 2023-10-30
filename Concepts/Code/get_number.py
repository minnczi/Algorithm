# 서울 5반 취향 반영 - shift 연산을 활용해서 만들어 봤어요
def BtoD(nbits, num):
    cnt = len(num)//nbits         # 숫자 개수
    mask_bits = ((1<<nbits) - 1)  # mask bit 작성 0b1111111  
    num = int(num, 2)             # 정수로 변경
    decimal = [(num >> (i*nbits)) & mask_bits for i in range(cnt)]
    return decimal
print(BtoD(7, '11001000000010')) 