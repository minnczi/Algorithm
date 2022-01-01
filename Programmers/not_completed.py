def solution(participant, completion):
    for person in participant:
        if person in completion:
            completion.pop(completion.index(person))
        else:
            return person