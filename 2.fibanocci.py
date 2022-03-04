num=int(input('Enter the limit'))
a=0
b=1
print(a)
print(b)
for i in range(2,num):
    value = a + b
    print(value)
    a = b
    b = value


