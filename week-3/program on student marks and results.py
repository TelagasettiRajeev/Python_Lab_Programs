def student_marks():
    python  = int(input("Enter marks in python: "))
    java  = int(input("Enter marks in java: "))
    kotlin  = int(input("Enter marks in kotlin: "))
    swift  = int(input("Enter marks in swift: "))
    go  = int(input("Enter marks in go: "))
    r  = int(input("Enter marks in r lang: "))
    total = python + java + kotlin + swift + go + r 
    percentage = ( total/6 )* 100
    return total, percentage


if __name__=="__main__":
    total, percentage = student_marks()
    print("Total marks : ", total )
    print("Percentage : ", percentage )