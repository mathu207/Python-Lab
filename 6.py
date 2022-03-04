string = input("enter the string: ")
frequencies = {}
for char in string:
    if char in frequencies:
       frequencies[char] += 1
    else:
         frequencies[char] = 1
print("Per char frequency in '{}' is : {}".format(string,str(frequencies)))