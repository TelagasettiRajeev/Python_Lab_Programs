class India:
    def capital( self ):
        print("New Delhi is the capital of India")
    def language( self ):
        print("Hindi is the most widely spoken language in india")
    def type( self ):
        print("India is a developing country")
        print('-' * 60 )

class USA:
    def capital( self ):
        print("Washington DC is the capital of USA")
    def language( self ):
        print("English is the most widely spoken language in USA")
    def type( self ):
        print("USA is a developed country")
        

obj1 = India()
obj2 = USA()

countries = [ obj1, obj2 ]
for country in countries:
    country.capital()
    country.language()
    country.type()
