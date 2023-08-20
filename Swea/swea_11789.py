# SWEA 11789
# 0과 1로 이루어진 1차 배열에서 7개 byte(글자)를 묶어서 10진수로 출력하기

T = int(input())


def bin_to_dec(num):
    dec_arr = []
    for i in range(0, len(num), 7):
        bin_num = num[i:i+7]
        dec_num = 0
        for j in range(7):
            if bin_num[j] == "1":
                dec_num += 2**(6-j)
        dec_arr.append(str(dec_num))
    return dec_arr


def bin_to_dec(num):
    dec_arr = []
    for i in range(0, len(num), 7):
        dec_arr.append(str(int(num[i:i+7], 2)))
    return dec_arr


def BtoD(byte, num):
    decimal = []
    for i in range(len(num)//byte):
        binary = num[i*byte:(i+1)*byte]
        d, b = 0, 1
        for j in range(byte-1, -1, -1):   # 0010101
            d += int(binary[j])*b
            b <<= 1
        decimal.append(str(d))
    return decimal


# def BtoD(byte, num):
#     rtn = []
#     for i in range(len(num)//byte):
#         binary = num[i*byte:(i+1)*byte][::-1]  # 뒤에서 읽기 위해 [::-1]
#         D = sum(int(binary[j]) & (1 << j) for j in range(byte))  # 10진수 변환
#         rtn.append(str(D))
#     return rtn


for tc in range(1, T+1):
    bit_num = input()
    print("#%d %s" % (tc, ", ".join(bin_to_dec(bit_num))))

print(BtoD(7, '1000101'))