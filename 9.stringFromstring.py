str1=input('Enter the string')
x=len(str1)
str2=str1[x-1]
#print(str1[x-1])
for i in range(1,x-1):
    str2=str2+str1[i]
str2=str2+str1[0]
print(str2)


