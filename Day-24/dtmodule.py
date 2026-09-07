from datetime import date,time,datetime,timedelta
t=date.today()
print(t)
print(t.day)
print(t.month)
print(t.year)
print(t.weekday())

#validating dob
year,month,day=list(map(int,input("[yyyy-mm-dd]").split('-')))
print(date(year,month,day))

#validating the time
tm = time(23,8,6)
print(tm)
print(tm.hour)
print(tm.minute)
print(tm.second)

dt=datetime.now()
print(dt)
print(dt.strftime('%d-%m-%y'))
print(dt.strftime('%d-%m-%Y'))#if we want hole year
print(dt.strftime('%d-%m-%Y %H:%M:%S'))#if we want time use %H:%M:%S
print(dt.strftime('%d-%m-%Y %H:%M:%S %p'))#if we want to know am or pm use p
print(dt.strftime('%d %b %Y %H:%T:%S %p'))#if we want month as string use b
print(dt.strftime('%d %B %Y %H:%T:%S %p'))#if we want hole month use B
print(dt.strftime('%a %b %Y %H:%T:%S %p'))#if we want day name use a
print(dt.strftime('%A %B %Y %H:%T:%S %p'))#if we want hole day use A
print(dt.strftime('%A %B %Y %i:%T:%S %p'))#if we want indian time use i

dt=datetime.now()
t=date.today()
print(t)
#if we wanto add or minus date or time we are using timedelta
t7=dt+timedelta(days=7)
print(dt)


m15=t+timedelta(minutes=15)
print(t7,m15)

from itertools import permutations,combinations
s='abc'
res1=list(permutations(s,2))
res2=list(combinations(s,2))

print([''.join(i) for i in res1])
print([''.join(i) for i in res2])


