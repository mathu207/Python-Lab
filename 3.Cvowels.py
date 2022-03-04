word=input('Enter the word')
print('Vowels in this word are:')
for i in range(0,len(word)):
    i=word[i]
    if i == 'a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U':
        print(i)
