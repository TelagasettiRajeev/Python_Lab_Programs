#creating userdefined exception
class NotEligibleForVote ( BaseException ):
    def __init__( self , msg ):
        self.msg = msg

#logic for checking voter age
class VoteEligible:
    def check_vote_eligibility( self, age ):
        try:
            if( age<18 ):
                raise NotEligibleForVote("Voter is not eligible for vote because age is lessthan 18..")
            else:
                print("You're eligible for vote...")
        except NotEligibleForVote as e:
            print( e )
        
#checking the user age for voting
age = int( input("Enter your age: "))
obj = VoteEligible()
obj.check_vote_eligibility( age )