dict = { 'langfounder':'G.V.Rossum' , 'language':'Python' , 'langcity':'Netherland' }
print("Dictionary : " , dict )

print( "language name : " , dict['language'] )

print("All keys in dictionary are : ")
for x in dict:
    print( x )

dict['langver'] = 3.11
print( "Updated dictionary : " , dict )

dict['language'] = 'java'
print( "Updated dictionary : " , dict )

print( "length of dictionary is ", len(dict) )

dict1 = dict.copy()
print("New dictionary : " , dict1 )

dict.clear()
print( "Updated dictionary : " , dict )