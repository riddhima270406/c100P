class atm(object):
    def __init__(self, card_no, pin_no):
        self.card_no = card_no
        self.pin_no = pin_no

    def balance_enquiry(self):
        print("Your balance is 1,00,000")

    def cash_withdrawl(self, amount):
        new_amount = 100000 - amount
        print("You have withdrawn amount "+ str(amount) + ". Your remaining balance is " + str(new_amount))


def main():
    Card_number = input("Insert your card number:- ")
    Pin_number = input("Enter your pin nmber:- ")

    new_user = atm(Card_number, Pin_number)

    print ("Choose your activity")
    print ("Activity 1 = Balance Enquiry")
    print ("Activity 2 = Cash Withdrawl")
    activity = int(input("Enter activity number:- "))

    if (activity == 1):
        new_user.balance_enquiry()
    elif (activity == 2):
        amount = int(input("Enter the amount you want to withdraw:- "))
        new_user.cash_withdrawl(amount)
    else:
        print("Enter a valid activity number.")

if __name__ == "__main__":
    main() 