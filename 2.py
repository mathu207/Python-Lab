#Anu Sunny
#21MCA_006
def file_read(fname):
    txt2 = open('D:/anu/pythonproject1/cycle5/text2.txt', 'w')
    with open(fname) as f:

        cont = f.readlines()
        for i in range(0, len(cont)):
            if (i % 2 !=0):
                txt2.write(cont[i])
            else:
                pass
    txt2.close()


    txt2 = open('D:/anu/pythonproject1/cycle5/text2.txt', 'r')


    cont1 = txt2.read()
    print(cont1)


file_read('D:/anu/pythonproject1/cycle5/test.txt')