num=int(input('Enter the size'))
Numbers=[]
print('Enter Numbers')
for i in range(0,num):
    x=int(input())
    Numbers.append(x)
print('the squares of number are:')
for i in Numbers:
    sqt=i * i
    print(sqt)

