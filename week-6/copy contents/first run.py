#creating a file with name "1st file" and write contents.

a = open( "1st_file.txt" , "w" )
a.write( "sample data...." )
a = open( "1st_file.txt" , "r" )
print( a.read() )

#creating an empty file
b = open( "2nd_file.txt" , "w" )
