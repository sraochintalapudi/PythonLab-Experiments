file1=input("Enter First Filename : ")
file2=input("Enter Second Filename : ")
# open file in read mode 
fn1 = open(file1, 'r') 

# open other file in write mode 
fn2 = open(file2, 'w') 

# read the content of the file line by line 
cont = fn1.readlines() 
#type(cont) 
for i in range(0, len(cont)):
    fn2.write(cont[i]) 

# close the file 
fn2.close() 
print("Content of first file copied to second file ")

# open file in read mode 
fn2 = open(file2, 'r') 

# read the content of the file 
cont1 = fn2.read() 

# print the content of the file 
print("Content of Second file :")
print(cont1) 

# close all files 
fn1.close() 
fn2.close()
