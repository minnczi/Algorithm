import sys
sys.stdin = open('input.txt')

decode = {
    '0001101': '0', '0011001': '1',
    '0010011': '2', '0111101': '3',
    '0100011': '4', '0110001': '5',
    '0101111': '6', '0111011': '7',
    '0110111': '8', '0001011': '9'}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 0

    # 1. 모든 중복없는 코드의 조합 가져오기
    codes = set()
    for i in range(N):
        codes |= set(input().split('0'))
    codes.remove('')
    
    
    for code in codes:
        # 2. 16진수 --> 2진수 변환
        while len(code) < 8:
            code += '0'
        print(code)
        binary = bin(int(code, 16))[2:].rstrip('0')
        binary = binary.zfill(round(len(binary)/56)*56)
        print(binary)

        # 3. 56자리보다 많다면, 56자리로 변환
        step = round(len(binary) / 56)
        binary_56 = ''
        for i in range(0, len(binary), step):
            binary_56 += binary[i]

        # 4. 코드 규칙에 따라 7자리씩 잘라서 2진수 --> 10진수 변환
        dec = []
        for i in range(0, 56, 7):
            dec.extend(map(int, decode[binary_56[i:i+7]]))
        
        # 4. 검증된 코드라면 자릿수의 합을 더해준다
        check = sum(dec[i] if i%2 else dec[i]*3 for i in range(7)) + dec[7]
        if check % 10 == 0:
            ans += sum(dec)
    print("#%d %d" % (tc, ans))

# print(codes)
# 0111011 / 0110001 / 0111011 / 0110001 / 0110001 / 0001101 / 0010011 / 0111011