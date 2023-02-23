class Student:
    __marks = []
    def set_data( self, r, n, m1, m2, m3 ):
        Student.__rollno = r
        Student.__name = n
        Student.__marks.append( m1 )
        Student.__marks.append( m2 )
        Student.__marks.append( m3 )
    def display_data( self ):
        print("Student Details :- ")
        print("Roll Number : ", Student.__rollno )
        print("Name : ", Student.__name )
        print("Marks : ", self.total() )
    def total( self ):
        m = Student.__marks
        return m[0]+m[1]+m[2]


r = int(input("Enter the roll number : ") )
n = input("Enter the name : ")
m1 = int(input("Enter the marks in first subject : "))
m2 = int(input("Enter the marks in second subject : "))
m3 = int(input("Enter the marks in third subject : "))

s1 = Student()
s1.set_data(r,n,m1,m2,m3)
s1.display_data()