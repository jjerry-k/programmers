import datetime
def solution(a, b):
    date = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return date[datetime.datetime(2016, a, b).weekday()]