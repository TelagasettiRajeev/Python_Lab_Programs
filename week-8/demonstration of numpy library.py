import numpy as np

#array creation
a = np.array( [ [1,2,3],[4,5,6] ] , dtype="float" )
print("Array created using passed list: \n" , a ) 

#array creation using tuple
b = np.array( (1,3,2) )
print("Array created using passed tuple: \n" , b )

# zeros array creation of 3x4 size
c = np.zeros( (3,4) )
print("Array initialized with all zeros: \n" , c )

# array creation using constant value of complex type
d = np.full( (4,4) , 9 , dtype="complex" )
print("Array initialized with all 9's\nArray type is complex:\n" , d )

#array creation with random values using random() function
e = np.random.random( (3,3) )
print("A random array : \n" , e )

#array creation with sequence using arange() function
f = np.arange( 0 , 30 , 5 )
print("A sequence array with steps of 5 : \n" , f )

#array with sequence of 10 values in range(0,5) using linspace()
g = np.linspace( 0, 5, 10)
print("Sequential array with 10 values between 0 and 5 : \n" , g )

#Reshaping 3x4 array to 2x2x3 array
arr = np.array( [ [1,2,3,4],[5,2,4,2],[1,2,0,1] ] )
newarr = arr.reshape( 2,2,3 )
print("Original array : \n" , arr )
print("Reshaped array : \n" , newarr )

#flatten array
arr = np.array( [ [1,2,3], [4,5,6] ] )
flarr = arr.flatten()
print("Original array : \n" , arr )
print("Reshaped array : \n" , flarr )