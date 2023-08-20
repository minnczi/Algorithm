hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def hex_to_bin(num):
    print(num)
    num = int(num) if num.isdigit() else hex_dict[num]
    bin_num = ""
    for j in range(3, -1, -1):
        if num & (1 << j):
            bin_num += '1'
        else:
            bin_num += '0'
    return bin_num


def bin_to_dec(num):
    dec_arr = []
    for i in range(0, len(num), 7):
        bin_num = num[i:i+7]
        dec_num = 0
        for j in range(len(bin_num)):
            if bin_num[j] == "1":
                dec_num += 2**(len(bin_num)-1-j)
        dec_arr.append(str(dec_num))
    return dec_arr


T = int(input())
for tc in range(1, T+1):
    hex_num = input()
    bin_num = ''
    for i in range(len(hex_num)):
        bin_num += hex_to_bin(hex_num[i])
    dec_arr = bin_to_dec(bin_num)
    print("#%d %s" % (tc, ", ".join(dec_arr)))
