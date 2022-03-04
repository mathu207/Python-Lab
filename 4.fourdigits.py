l1=int(input('Enter the start'))
l2=int(input('Enter the end '))

for i in range(l1,l2):
   str1=str(i)
   if(int(str1[0])%2 == 0 and int(str1[1]) % 2==0 and int(str1[2])%2 ==0 and int(str1[3])%2==0 ):
       for j in range(1,i+1):
           if j*j==i:
               print(i)

