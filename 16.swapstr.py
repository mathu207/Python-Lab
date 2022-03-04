str1=input('Enter string1')
str2=input('Enter string2')
x=str1[0:1]
str1=str1.replace(str1[0:1],str2[0:1])
str2=str2.replace(str2[0:1],x)

newStr=str1+' '+str2
print(newStr)
