str=input('Enter the string')
x=len(str)
if(str[-3:]=='ing'):
   str=str+'ly'
else:
   str=str+'ing'

print('\n the string is ',str)

