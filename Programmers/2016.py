def solution(a, b):
    #달별로 한달에 몇일이 있는지 저장하는 리스트
    days_in_a_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    nth_day = sum(days_in_a_month[0:a-1]) + b

    day_of_week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    return day_of_week[nth_day % 7]