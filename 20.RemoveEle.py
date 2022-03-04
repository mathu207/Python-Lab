n=int(input('Enter the no fo elements for list'))
list=[]
list2=[]
print('Enter the elements')
for i in range(0,n):
    x=int(input())
    list.append(x)
for i in range(0,len(list)):
    if(list[i]%2==0):
        pass
    else:
        list2.append(list[i])
print('The even numbers removed list is',list2)

