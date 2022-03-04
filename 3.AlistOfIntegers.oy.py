n=int(input('Enter The no of elements'))
Numbers=[]
print('enter the elements')
for i in range(0,n):
    num=int(input())
    Numbers.append(num)
#print(Numbers)
print('positive integers are:')
for i in Numbers:
    if i >= 0:
        print(i)






