number=int(input("enter a number "))
print("factors of {} are".format(number))
for i in range(1,number+1):
    if number%i ==0:
        print(i)