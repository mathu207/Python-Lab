#Anu Sunny
#21MCA_006
class Bank_Account:
    def __init__(self,accno,name,typeacc,balance):
        self.accno=accno
        self.name=name
        self.typeacc=typeacc
        self.balance =balance

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\n Account no (A\C)=", self.accno)
        print("\n Name =", self.name)
        print("\n Type Of Account =", self.typeacc)
        print("\n Net Available Balance=", self.balance)

ano=int(input('Enter Account no'))
name=input('Enter Name')
type=input('Enter Account type')
balance=int(input('Enter account balance'))
s = Bank_Account(ano,name,type,balance)
s.deposit()
s.withdraw()
s.display()