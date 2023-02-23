class Account:
    def __init__( self ):
        self.balance = 0
        print("New account created")
    def deposit( self ):
        amount = float(input("Enter the amount to deposit: "))
        self.balance += amount
        print("New Balance : %f" %self.balance)
    def withdraw( self ):
        amount = float(input("Enter the amount to withdraw: "))
        if( amount < self.balance ):
            self.balance -= amount
            print("New Balance : %f" %self.balance)
        else:
            print("Insufficient balance")
    def enquiry( self ):
        print("Balance : %f" %self.balance )

a = Account()
a.deposit()
a.withdraw()
a.enquiry()
