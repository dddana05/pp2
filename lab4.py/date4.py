import datetime 
today = datetime.datetime.now()
bday =  datetime.datetime(2023,3,18,11,58)
time_diff=bday-today
print(time_diff)
seconds=time_diff.seconds
print({seconds})


