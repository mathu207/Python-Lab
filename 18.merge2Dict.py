n=int(input('Enter the size of dict1'))
d={}
print("enter elements")
for i in range(n):
    keys=input()
    values=input()
    d[keys]=values


n=int(input('Enter the size of dict2'))
d2={}
print("enter elements")
for i in range(n):
    keys=input()
    values=input()
    d2[keys]=values
print("Dict 1 :",d)
print("Dict 2 :",d2)
#d3=d+d2

d3=d.copy()
for key,value in d2.items():
    d3[key]=value
print("Merged dict :",d3)

#dcomp={key: d[key] + d2[key] for key in d}
#print("dcomp",dcomp)
#dcomp={key:[ d[key] ,d2[key]] for key in d}