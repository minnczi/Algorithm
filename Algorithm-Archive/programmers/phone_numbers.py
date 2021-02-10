#내 풀이
def solution(phone_book):
    for i in range(0, len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if len(phone_book[i]) <= len(phone_book[j]):
                short, long = phone_book[i], phone_book[j]
            else:
                short, long = phone_book[j], phone_book[i]

            if short == long[0:len(short)]:
                return False
    return True

#해쉬 사용한 풀이
def solution2(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

#다른 깔끔한 풀이
def solution3(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


from itertools import combinations as c
def solution4(phoneBook):
    answer = True
    sortedPB = sorted(phoneBook, key= len)
    for (a,b) in c( sortedPB,2):
        if a == b[:len(a)]:
            answer = False
    return answer