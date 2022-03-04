n=int(input('Enter list1 size'))
list1=[]
sum1=0
sum2=0
print('Enter the values for list1 ')
for i in range(0,n):
    x=int(input())
    list1.append(x)
n2=int(input('Enter list2 size'))
list2=[]
print('Enter the values for list2')
for i in range(0,n2):
    y=int(input())
    list2.append(y)
if(len(list1)==len(list2)):
    print('\n >> Two lists are of same length',len(list1))
else:
    print('\n >> The to list are of different length,length of list1 is {0} and list2 is {1}'.format(len(list1),len(list2)))

for i in range(0,n,1):
    sum1=int(sum1)+list1[i]
for j in range(0,n2,1):
    sum2=int(sum2)+list2[j]
if(sum1==sum2):
    print('\n >> The sum of both list are equal and sum is ',sum1)
else:
    print('\n >> The sums of both list are different,the sum of list1 is {},\n sum of list2 is {}'.format(sum1,sum2))

if(set(list1)&set(list2)):
    print('\n >> The values common in both list are',set(list1)&set(list2))
else:
    print('\n no common elements in both list')