

file1 = input("Enter first filename : ")
file2 = input("Enter second filename : ")

#open file1 in read mode
fn1 = open( file1 , "r" )

#open file2 in write mode
fn2 = open( file2 , "w" )

#read the content of the file line by line
cont = fn1.readlines()

#write content
for i in range( 0 , len(cont) ):
    fn2.write( cont[i] )

#close the file 
fn2.close()

print( "Content of first file copied to second file" )

#open file2 in read mode
fn2 = open( file2 , "r" )

#read the content of the file
cont1 = fn2.read()

#print the content of the file 
print("Content of second file: ")
print( cont1 )

#close all files
fn1.close()
fn2.close()