import datetime

def do_datetime_stuff():
    #get the current time
    now = datetime.datetime.now()
    print(now)
    
    #get the current time(formatted)
    now_formatted = now.strftime("%Y/%m/%d %H:%M")
    print(now_formatted)

    #get the current date
    today = datetime.date.today()
    print(today)
    yesterday = today-datetime.timedelta(days=1)
    print(yesterday)

do_datetime_stuff()