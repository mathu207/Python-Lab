import datetime
#currentYr=int(input('Enter current year'))
finalYr=int(input('Enter final year'))
now = datetime.datetime.now().year
#print(now)
for i in range(now,finalYr+1):
    if i % 4 == 0 and i % 100 !=0:
        print(i)
    elif i % 400 ==0:
        print(i)


