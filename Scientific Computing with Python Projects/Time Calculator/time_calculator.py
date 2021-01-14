

def add_time(start, duration, day = ""):
    parse_arr = start.split()
    start_m = parse_arr[1]
    parse_arr = parse_arr[0].split(":")
    start_hour = int(parse_arr[0])
    start_minute = int(parse_arr[1])

    if start_m == "PM" :
        start_hour += 12
    if start_hour == 12 :
        start_hour = 0
    elif start_hour == 24 :
        start_hour = 12
    #print(start_hour,":",start_minute)

    parse_arr = duration.split(":")
    duration_hour = int(parse_arr[0])
    duration_minute = int(parse_arr[1])
    #print(duration_hour,":",duration_minute)

    start_hour+=duration_hour
    start_minute+=duration_minute
    if start_minute >= 60 :
        start_hour+=1
        start_minute-= 60
    #print(start_hour,":",start_minute)

    days = 0
    while start_hour >= 24 :
        start_hour-=24
        days+=1
    answer = ""
    m = "AM"
    if start_hour > 12 :
        m = "PM"
        start_hour-=12
    elif start_hour == 12 :
        m = "PM"
    elif start_hour == 0 :
        start_hour+=12
    zero = ""
    if start_minute < 10 :
        zero = "0"
    day_info = " ("+str(days)+" days later)"
    if days == 0 :
        day_info = ""
    elif days == 1 :
        day_info = " (next day)"
    if day != "" :
        d = {"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
        day_num = 0
        try :
            day_num = d.get(day.lower())
        except :
            day = ""
        if day != "" :
            day_num+=days
            day_num%=7

            for i in d :
                if day_num == d[i] :
                    day = i
                    day=day[:1].upper()+day[1:]
                    break
            day = ", "+day
    answer+=str(start_hour)+":"+ zero+str(start_minute)+" "+m+day+day_info
    return answer
