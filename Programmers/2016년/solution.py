def solution(a, b):
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    for i in range(a-1):
        b += months[i]
    return days[(b%7)-1]
