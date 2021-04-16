import os

file1 = open('Aptech_Work/Filing/demo/newfile.txt','w')

print('Enter in file')

file1.write(input("New in : "))

file1.close()

#read files

readfiles  = open('Aptech_Work/Filing/demo/newfile.txt','r')

reader = readfiles.read()

print(reader)


#path
change = input('Change Path : Y or else : ')

if(change == 'Y'):
    print(os.getcwd())

    os.chdir('demo\changepath')

    print(os.getcwd())
else:
    print("Path No Change")

#apend

file2forapend = open('Aptech_Work/Filing/demo/newfile.txt','a')

print('Enter in file for apend')

file2forapend.write(input("New in : "))

file2forapend.close()


readfiles2  = open('Aptech_Work/Filing/demo/newfile.txt','r')

reader2 = readfiles2.read()

print(reader2)

#split

splitfile = readfiles2.read()

print(splitfile.split())

readfiles2.close()