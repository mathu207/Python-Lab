n=int(input("eneter no of number"))
Numbers=[]
print('eneter value')
for i in range(0,n):
    x=int(input())
    if(x>100):
        Numbers.append('over')
    else:
        Numbers.append(x)
print('The elements are')
print(Numbers)