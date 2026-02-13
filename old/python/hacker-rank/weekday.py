import calendar

if __name__ == "__main__":
    month, day, year = list(map(int, input().strip().split()))
    weekday = calendar.weekday(year, month, day)
    print(calendar.day_name[weekday].upper())