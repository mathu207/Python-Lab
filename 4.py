#Anu Sunny
#21MCA_006

class Time:
    def __init__(self,hour,min,sec):
        self.hour=hour
        self.min=min
        self.sec=sec

    def __add__(self,second):
        hours=self.hour + second.hour
        mins= self.min + second.min
        secs= self.sec + second.sec
        print(hours,'hours',mins,'minues',secs,'seconds')

print('Enter hour ,minute and second for 1')
h,m,s=int(input()),int(input()),int(input())
print('Enter hou,min,sec for 2')
h1,m1,s1=int(input()),int(input()),int(input())

t1=Time(h,m,s)
t2=Time(h1,m1,s1)

print('\nsum of time:')
t1 + t2

