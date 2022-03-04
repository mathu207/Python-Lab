n1=int(input('Enter first number'))
n2=int(input('Enter the second number'))
for i in range(1,n1 and n2):
    if(n1%i==0 and n2%i==0):
        gcd=i
print('The GCD of {} and {} is {}'.format(n1,n2,gcd))