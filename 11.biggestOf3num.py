n1=int(input('enter first number'))
n2=int(input('enter second number'))
n3=int(input('enter third number'))
if n1>n2:
    if n1>n3:
        print('\n Largest Number is :',n1)
    else:
        print('\n largest number is',n3)
elif n2>n3:
    print('\n Largest number is ',n2)
else:
    print('\n Largest numbers is ',n3)
