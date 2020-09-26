def similar_words(word1, word2):
    diff = 0
    for i in range (0, len(word1)):
        if word1[i] != word2[i]:
            diff += 1
    if diff == 1:
        return True
    else:
        return False
               
def solution(begin, target, words):
    print(similar_words("hat", "bat"))
    print(similar_words("hat", "cap"))
    print(begin[0])
    print(len(begin))

# visited_list = []
# answer = 0

# def solution(begin, target, words):
#     global answer
#     queue = [begin]
#     #word list에 있고 아직 방문하지 않은 단어중에서
#     while queue:
#         current_word = queue.pop(0)
#         visited_list.append(current_word)
#         print("current word:", current_word)
#         #만약 word=target이면 바로 답 반환
#         if current_word == target:
#             return answer
#         #begin과 word가 정확히 1글자 차이나는지 검증
#         else:
#             difference = 0
#             for word in words:
#                 print(word)
#                 if word in visited_list:
#                     continue
#                 else:
#                     for i in range(0, len(current_word)):
#                         #만약 두글자 이상 다를 경우 불가능이므로 break
#                         if difference >= 2:
#                             break
#                         #한글자가 다를때마다 += 1
#                         elif word[i] != begin[i]:
#                             difference += 1
#                         #정확히 한글자 차이나는 단어들을 queue에 넣기
#                         if difference == 1:
#                             queue.append(word)
#         answer += 1
#     return answer