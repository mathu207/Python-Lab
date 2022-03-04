num=int(input('Enter no of names'))
names=[]
count=0
print('Enter the students name')
for i in range(0,num):
    x=input()
    names.append(x)
for name in names:
    for i in range(0,len(name)):
        y=name[i]
        if y=='a':
            count=count+1
print('no of occurence of a',count)

