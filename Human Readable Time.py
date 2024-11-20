def make_readable(seconds):
    time = ''
    ss, mm, hh = '', '', ''
    if seconds == 0:
        time = '00:00:00'
        return time
    elif seconds >= 359999:
        time = '99:59:59'
        return time
    if seconds < 60:
        mm = ':00'
        hh = '00'
    elif seconds < 6000:
        hh = '00'
    if int(str(seconds)[-2:]) <= 59:
        ss = ':' + str(seconds)[-2:]
    else:
        ss = ':' + str(int(str(seconds)[-2:]) - 60)
    print(ss)
    print(str(seconds)[-4:-3])
    print(str(seconds)[:-5])
    # if int(str(seconds)[-4:-3]) <= 59:
    #     hh = ':' + str(seconds)[-4:-3]
    # else:
    #     ss = ':' + str(int(str(seconds)[-4:-3]) - 60)
        
    time = hh + mm + ss
    return time



print(make_readable(0))
print(make_readable(59))
print(make_readable(3599))
print(make_readable(3600))
print(make_readable(35999))