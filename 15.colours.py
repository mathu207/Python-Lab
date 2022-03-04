n1=int(input('enter no of colours for list1'))
list1=[]
print('enter the colours for list1')
for i in range(0,n1):
    x=input()
    list1.append(x)
n2=int(input('enter no of colours for list2'))
list2=[]
print('enter colours for list2')
for i in range(0,n2):
    x=input()
    list2.append(x)
print('colours that in list2 not in list1 are: ',set(list2)-set(list1))
