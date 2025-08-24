def add_time(start_time, duration_time, start_day=None):
    n = 0 #number of days
    final_day = ""
    if start_day:
        start_day = start_day.capitalize()
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


    #Spliting Start Time 
    start_time, clock_system = start_time.split(" ")
    start_hour, start_minute = start_time.split(":")
    start_hour = int(start_hour)

    #Spliting Duration Time
    duration_hour, duration_minute = duration_time.split(":")

    if clock_system == "PM":
        start_hour += 12
    
    total_hour = int(start_hour) + int(duration_hour)
    total_minute = int(start_minute) + int(duration_minute)
    if total_minute > 59:
        total_hour += total_minute // 60
        total_minute = total_minute % 60
        
    if total_hour > 23 and total_hour >= 0:
        n += total_hour // 24 
        total_hour %= 24


    if total_hour >= 12 :
        clock_system = "PM"
    elif total_hour < 12:
        clock_system = "AM"

    if clock_system == "PM":
        total_hour -= 12

    if total_hour == 0:
        total_hour = 12

    if start_day:    
        final_day = days[(days.index(start_day) + n )% 7 ].capitalize()
        if n == 1:
            return f"{total_hour}:{total_minute:02} {clock_system} {final_day} (next day)"

        elif n > 1:
            pass
            return f"{total_hour:02}:{total_minute:02} {clock_system} {final_day} ({n} days later)"

        else:
            return f"{total_hour:02}:{total_minute:02} {clock_system} {final_day}"
    else:
        if n == 1:
            return f"{total_hour}:{total_minute:02} {clock_system} (next day)"

        elif n > 1:
            return f"{total_hour:02}:{total_minute:02} {clock_system} ({n} days later)"

        else:
            return f"{total_hour:02}:{total_minute:02} {clock_system}"

print(add_time('8:16 PM', '466:02', 'tuesday'))
