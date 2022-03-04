text=input('Enter Text')
word=input('Enter word to search')
temp=[]
count=0
temp=text.split(" ")
for i in range(0,len(temp)):
    if word==temp[i]:
        count=count+1
print('count of occurence of word :',count)
