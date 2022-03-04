#Anu Sunny
#21MCA_006
def file_read(fname):
    with open(fname) as f:

        content_list = f.readlines()
        print(content_list)


file_read('D:/anu/pythonproject1/cycle5/test.txt')