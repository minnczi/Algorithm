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

for tc in range(1, T+1):
    bit_num = input()
    print("#%d %s" % (tc, ", ".join(bin_to_dec(bit_num))))