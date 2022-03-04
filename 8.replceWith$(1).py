str1=input('Enter the string')
x=len(str1)
firstValue=str1[0]
str2=firstValue
for i in range(1,x):
    if firstValue==str1[i]:
        str2=str2+'$'
    else:
        str2=str2+str1[i]
print('After replacement')
print(str2)