n=int(input("Enter the step number"))
for i in range(1,n+1):
   j=i
   for k in range(1,i+1):
       print('\t',j,end="")
       j=j+i
   print('\r')
