from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2015, 12, 20)
end_dt = date(2016, 1, 11)

# for dt in daterange(start_dt, end_dt):
#     print(dt.strftime("%m-%d-%Y"))

print(daterange(start_dt, end_dt).strftime("%m-%d-%Y"))