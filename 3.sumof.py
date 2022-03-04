n=int(input('Enter the size of list'))
list=[]
sum=0
print('Enter the elements')
for i in range(n):
   x=int(input())
   list.append(x)
for i in range(0,len(list)):
   sum=sum+list[i]
print("Sum of the elements in the list is ",sum)
