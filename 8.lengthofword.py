n=int(input('enter th no of words'))
list1=[]
for i in range(0,n):
   x=input()
   list1.append(x)
long=len(list1[0])
print(long)
for i in range(1,len(list1)):
   if(len(list1[i])>long):
       long=list1[i]
print(list1[i])
print(long)
