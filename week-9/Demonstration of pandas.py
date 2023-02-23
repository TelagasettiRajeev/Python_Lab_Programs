import pandas as pd

d1 = { 'name':'student1' , 'sub1':90 , 'sub2':92 , 'sub3':94 , 'sub4':96 , 'sub5':98 , 'sub6':100 }
d2 = { 'name':'student2' , 'sub1':80 , 'sub2':82 , 'sub3':84 , 'sub4':86 , 'sub5':88 , 'sub6':90 }
d3 = { 'name':'student3' , 'sub1':70 , 'sub2':72 , 'sub3':74 , 'sub4':76 , 'sub5':78 , 'sub6':80 }
d4 = { 'name':'student4' , 'sub1':60 , 'sub2':62 , 'sub3':64 , 'sub4':66 , 'sub5':68 , 'sub6':70 }

l = [ d1 , d2 , d3 , d4 ]
data = pd.DataFrame( l , index=['s1' , 's2' , 's3' , 's4'] )
print( data )

data['total'] = data['sub1'] + data['sub2'] + data['sub3'] + data['sub4'] + data['sub5'] + data['sub6'] 

print("Before deleting total column")
print( '-' * 60 )
print( data )
print()

print("After deleting total column ")
print( '-' * 60 )
d = data.drop( 'total' , axis=1 )
print( d )
print()

print("After deleting s4 row ")
print( '-' * 60 )
d = data.drop( 's4' , axis=0 )
print( d )
print()
