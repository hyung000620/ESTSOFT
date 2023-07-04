from datetime import datetime,timedelta

now = datetime.now()
f_time = now.strftime("%Y/%m/%d, %H:%M:%S")
print("형식 시간: ", f_time)

day_before = now -timedelta(days=1)
print("하루 전: ",day_before)
