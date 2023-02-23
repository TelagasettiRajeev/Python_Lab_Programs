
class parentClass:
    def method1( self ):
        print("Parent Class - method1 ")
    def method2( self ):
        print("Parent Class - method2 ")
class childClass( parentClass ):
    def method2( self ):
        print("Child Class - method2 ")
    def method3( self ):
        print("Child Class - method3 ")
    
def main():
    c = childClass()
    c.method1()
    c.method2()
    c.method3()

if __name__ == "__main__":
    main()